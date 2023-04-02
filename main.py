import streamlit as st
import openai
from prompts import award_dict, tier_dict, sq_pri_dict, wg_pri_dict

import sys
sys.path.append('.')
from engine import EvaluatorEngine

def app():

    # Page Config :fishing_pole_and_fish:
    st.set_page_config(
        page_title='Fisch Rank',
        page_icon=':fishing_pole_and_fish:',
        layout='wide',
        initial_sidebar_state='expanded',
        menu_items={
            'Get Help': None,
            'Report a bug': 'mailto:levon.fischer@gmail.com',
            'About': None
        }
    )
    # Some stateful variables
    if 'latest_insertions' not in st.session_state:
        st.session_state['latest_insertions'] = None
    if 'insertion_cancelled' not in st.session_state:
        st.session_state['insertion_cancelled'] = False

    # Set up the engine
    @st.cache(allow_output_mutation=True)
    def create_engine():
        return EvaluatorEngine()
    engine = create_engine()


    st.title('The Fisch Rank')
    st.write('A simple app to evaluate a performance statement and then dump it into a database to query it later.')

    ###########
    # Sidebar #
    ###########

    # Get the OpenAI API key, whether from the OPENAI_API_KEY environment variable or from user input.
    st.sidebar.header("Parameters")

    user = st.sidebar.text_input(label= 'User',
                                 value= 'Levon')

    token = st.sidebar.text_input(label= 'OpenAI API access token',
                                  value= openai.api_key if openai.api_key is not None else '',
                                  type = 'password',
                                  help = 'Get it on https://beta.openai.com/')

    engine.gpt_parameters['engine'] = st.sidebar.text_input('GPT Engine', 'gpt-3.5-turbo')
    engine.gpt_parameters['temperature'] = st.sidebar.slider('GPT Temperature',
                                                             value = 0.7,
                                                             min_value = 0.0,
                                                             max_value= 1.0,
                                                             step = 0.1)
    engine.gpt_parameters['frequency_penalty'] = st.sidebar.slider('GPT Frequency Penalty',
                                                                   value=0.0,
                                                                   min_value=0.0,
                                                                   max_value=1.0,
                                                                   step=0.1)
    engine.gpt_parameters['presence_penalty'] = st.sidebar.slider('GPT Presence Penalty',
                                                                  value=0.0,
                                                                  min_value=0.0,
                                                                  max_value=1.0,
                                                                  step=0.1)

    engine.set_openai_api_key(token)

    # We have different tabs for searching and for statement evaluation
    tab1, tab2 = st.tabs(['Evaluate Statement', 'Search Statements'])

    ################
    # Evaluate tab #
    ################

    with tab1:
        #Make buttons to select Tier, Award, and category
        col1, col2, col3, col4 = st.columns(4)
        engine.statement_parameters['tier'] = col1.selectbox(label='Tier',
                                                             options=tier_dict,
                                                             index=0)
        engine.statement_parameters['award'] = col2.selectbox(label='Award',
                                               options=award_dict,
                                               index=0)
        engine.statement_parameters['sq'] = col3.selectbox(label='Squadron',
                                            options=sq_pri_dict,
                                            index=0)
        engine.statement_parameters['wg'] = col4.selectbox(label='Wing',
                                            options=wg_pri_dict,
                                            index=0)

        st.text('Paste the performance statement to be evaluated')
        with st.form('new_statement_form', clear_on_submit=True):
            new_statement_utterance = st.text_input('New Performance Statement', '', help='Paste your statement here.')
            user_score = st.number_input('Predicted Score', min_value=0.0, max_value=20.0, value=10.0, step=0.5)
            add_statement = st.form_submit_button('Evaluate')

        manual_check = st.checkbox('Check before adding', value = True)

        # placeholder for where the manual check pane will be
        manual_check_pane = st.empty()

        # auxiliary function to commit extraction, will be used more than once below
        def aux_commit_extraction():
            st.session_state['latest_insertions'] = engine.extracted_evaluation()
            engine.commit()

        #
        # EXTRACT: If we don't have an extracted statement yet, let's try to do that.
        #
        if not engine.has_extracted_statement():
            if add_statement:
                engine.extract_evaluation(new_statement_utterance, user, user_score)

        #
        # COMMIT: If now we have the extracted statement, prepare to commit or commit them directly.
        #
        if engine.has_extracted_statement():

            # does the user want to manually check the extracted facts?
            if manual_check:

                with manual_check_pane.container():

                    st.write('Extracted statement:')
                    st.write(engine.extracted_evaluation())
                    accept = st.button('Accept Score')
                    cancel = st.button('Cancel Score')

                    if accept:
                        aux_commit_extraction()

                    elif cancel:
                        engine.cancel()
                        st.session_state['insertion_cancelled'] = True

            else: # no manual check needed, lets just commit
                aux_commit_extraction()

    with tab2:
        st.text('Database and Search coming soon.')

    ###################
    # Status messages #
    ###################

    if st.session_state['latest_insertions'] is not None:
        st.success(f'Added {st.session_state["latest_insertions"]} statements to the database.')
        st.session_state['latest_insertions'] = None
        manual_check_pane.empty()
    elif st.session_state['insertion_cancelled']:
        st.info('Insertion cancelled.')
        st.session_state['insertion_cancelled'] = False
        manual_check_pane.empty()


if __name__ == '__main__':
    app()