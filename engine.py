import openai
import os
import io
import pandas as pd
import logging

import streamlit as st

from prompts import *

class EvaluatorEngine:
    """
    The main class of the Evaluator engine. It stores the database and application parameters, as well as
    coordinates the calls to GPT-3 model, leveraging the preprocessor and postprocessor. In this manner,
    it provides the capability both to insert new statements and to query the database.
    """

    def __init__(self, api_key = st.secrets["OPENAI_API_KEY"],
                 database_file_path = './data/default_database.csv',
                 gpt_engine = 'gpt-3.5-turbo',
                 gpt_temperature=0.7):
        self._database_file_path = database_file_path

        # Load the database or create it from scratch if needed
        try:
            self.database = pd.read_csv(self._database_file_path)
            logging.info(f'Loaded database from {self._database_file_path}.')
        except FileNotFoundError:
            self.database = pd.DataFrame(columns=['statement', 'tier', 'award', 'category', 'score'])
            self._save()
            logging.info(f'Created database in {self._database_file_path}')


        openai.api_key = api_key
        self.gpt_parameters = {'engine': gpt_engine,
                               'temperature': gpt_temperature,
                               'max_tokens': 1000,
                               'top_p': 1.0,
                               'frequency_penalty': 0.0,
                               'presence_penalty': 0.0,
                               'stop': None}

        self._current_extracted_statement = None

        # Create preprocessor and postprocessor for GPT inputs and outputs
        self._preprocessor = StatementPreprocessor()
        self._postprocessor = StatementPostprocessor()

    def _save(self):
        logging.info(f'Database has {len(self.database)} facts.')

        self.database.to_csv(self._database_file_path, index=False)

        logging.info(f'Saved database in {self._database_file_path}.')

    ####################################
    # Facts insertion workflow methods #
    ####################################

    def extract_statement(self, statement_utterance, award, tier, wg, sq):
        """
        Extracts facts from a natural language utterance. Returns a list of tuples (statement, tier, award, category, score).
        """

        statement_tuples = self._postprocessor.string_to_tuples(self._gpt_chat(self._preprocessor.extraction_prompt(statement_utterance, award, tier, wg, sq)))
        self._current_extracted_statement = statement_tuples
        return statement_tuples

    def has_extracted_statement(self):
        return self._current_extracted_statement is not None

    def extracted_statement(self):
        """
        Returns the current extracted statement as a list of dictionaries, for readability.
        """
        return[{'Statement': state[0], 'Tier': state[1], 'Award': state[2], 'Category': state[3], 'Score': state[4]}
               for state in self._current_extracted_statement]

    def commit(self):
        """
        Commits the current statement to the database. If no statement has been extracted,
        the method just does nothing.
        """
        if self._current_extracted_statement is not None:
            self._insert_statement()
            self._current_extracted_statement = None
            self._save()
        else:
            logging.info("Nothing to commit.")

    def cancel(self):
        """
        Cancel the current extracted facts. If no facts have been extracted, the method just does nothing.
        """
        if self._current_extracted_statement is not None:
            self._current_extracted_statement = None
        else:
            logging.info('Nothing to revert')

    def _insert_statement(self, statement_utterance = None):
        """
        Inserts a statement into the database.
        """

        # reuse the extracted statement, if any
        if self._current_extracted_statement is None:
            statement_tuples = self.extract_statement(statement_utterance)
        else:
            statement_tuples = self._current_extracted_statement

        for statement_tuple in statement_tuples:
            logging.info(f'Database has {len(self.database)} statements before insertion.')
            logging.info(f'Inserting statement: {statement_tuple}')

            df_to_add = pd.DataFrame([statement_tuple], columns=['statement', 'tier', 'award', 'category', 'score'])
            self.database = pd.concat([self.database, df_to_add], ignore_index=True)

            logging.info(f'Database has {len(self.database)} statements after insertion.')

    ###########
    # GPT API #
    ###########

    def _gpt_complete(self, prompt, echo=False):
        ### Likely to be replaced with _gpt_chat
        response = openai.Completion.create(
            engine = self.gpt_parameters['engine'],
            prompt = prompt,
            temperature = self.gpt_parameters['temperature'],
            max_tokens = self.gpt_parameters['max_tokens'],
            top_p = self.gpt_parameters['top_p'],
            frequency_penalty = self.gpt_parameters['frequency_penalty'],
            presence_penalty = self.gpt_parameters['presence_penalty'],
            stop = self.gpt_parameters['stop'],
            echo = echo
        )

        completion = response['choices'][0]['text']

        return completion

    def _gpt_chat(self, messages, stream=False, echo=False):

        response = openai.ChatCompletion.create(
            model = self.gpt_parameters['engine'],
            messages = messages,
            temperature = self.gpt_parameters['temperature'],
            top_p = self.gpt_parameters['top_p'],
            stream = stream,
            stop = self.gpt_parameters['stop'],
            max_tokens = self.gpt_parameters['max_tokens'],
            presence_penalty = self.gpt_parameters['presence_penalty'],
            frequency_penalty = self.gpt_parameters['frequency_penalty'],
            #user = user
        )

        completion = response['choices'][0]['message']['content']

        return completion

    def set_openai_api_key(self, key):
        openai.api_key = key

    ##################
    # Data utilities #
    ##################

    def export_data_to_binary(self, df, file_type=None):
        if file_type is None:
            file_type = 'excel'

        if file_type == 'excel':
            memory_output = io.BytesIO()
            with pd.ExcelWriter(memory_output) as writer:
                df.to_excel(writer)
            return memory_output

        elif file_type == 'csv':
            return df.to_csv().encode('utf-8')

        elif file_type == 'tsv':
            return df.to_csv(sep='\t').encode('utf-8')

        else:
            return ValueError('Invalid file type.')

class StatementPreprocessor:
    """
    Preprocessor for the user input to GPT. Notably, includes the mechanisms to build prompts.
    """

    def extraction_prompt(self, x, award, tier, wg, sq):

        main_prompt = \
f"""
This is the definition of a performance statement:
    {OVERVIEW}
    This is the definition of the award you are grading for:
    {award_dict[award]}
    This is the award nominee's rank tier and the expectations for that tier that you should take into account when grading:
    {tier_dict[tier]}
    This is the Wing Commander's priorities that you should take into account when grading:
    {wg_pri_dict[wg]}
    This is the Squadron Commander's priorities that you should take into account when grading:
    {sq_pri_dict[sq]}
    These are the Airman Leadership Qualities that you should grade the performance statement on:
    {ALQ}
"""
        messages = [
            {'role': 'system', 'content': SYSTEM},
            {'role': 'user', 'content': main_prompt},
            {'role': 'system', 'name': 'example_user', 'content': examples[0][0]},
            {'role': 'system', 'name': 'example_assistant', 'content': examples[0][1]},
            {'role': 'system', 'name': 'example_user', 'content': examples[1][0]},
            {'role': 'system', 'name': 'example_assistant', 'content': examples[1][0]},
            {'role': 'user', 'content': x}
        ]
        logging.info(f'GPT Prompt: {messages}')
        return messages

class StatementPostprocessor:
    """
    Postprocessor for the GPT raw outputs.
    """

    def extract_score_from_result(self, result):
        """
        Extracts the score from the result string
        """
        score = result[-6:]
        return score

    def string_to_tuples(self, s):
        """
        Converts a string that looks like a tuple to an actual Python tuple.
        """
        return [eval(s.strip()) for s in self.extract_score_from_result(s)]