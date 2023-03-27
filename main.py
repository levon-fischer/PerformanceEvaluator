import streamlit as st
import openai

import sys
sys.path.append('.')
from engine import EvaluatorEngine

def app():

    # Page Config
    st.set_page_config(
        page_title='Performance Evaluator',
        layout='wide',
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


    st.title('Performance Statement Evaluator')
    st.write('A simple app to evaluate a performance statement and then dump it into a database to query it later.')

    ###########
    # Sidebar #
    ###########

    # Get the OpenAI API key, whether from the OPENAI_API_KEY environment variable or from user input.
    st.sidebar.header("Parameters")

    token = st.sidebar.text_input('OpenAI API access token',
                                  openai.api_key if openai.api_key is not None else '',
                                  type = 'password',
                                  help = 'Get it on https://beta.openai.com/')

    engine.gpt_parameters['engine'] = st.sidebar.text_input('GPT Engine', 'text-davinci-003')
    engine.gpt_parameters['temperature'] = st.sidebar.slider('GPT Temperature',
                                                             value = 0.1,
                                                             min_value = 0.0,
                                                             max_value= 1.0,
                                                             step = 0.1)

    engine.set_openai_api_key(token)

    # We have different tabs for searching and for statement evaluation
    tab1, tab2 = st.tabs(['Evaluate Statement', 'Search Statements'])

    ################
    # Evaluate tab #
    ################

    with tab1:
        #Make buttons to select Tier, Award, and category
        col1, col2, col3 = st.columns(3)
        tier = col1.selectbox(label='Tier',
                              options=('Junior Enlisted', 'NCO', 'SNCO', 'CGO', 'FGO', 'N/A'),
                              index=0)
        award = col2.selectbox(lable='Award',
                               options=('___ of the Quarter', 'ISR Tech', 'Volunteer'),
                               index=0)
        category = col3.selectbox(lable='Category',
                                  options=('Primary Duties', 'Followership/Leadership', 'Whole Airman Concept'),
                                  index=0)

        st.text('Past the performance statement to be evaluated')
        with st.form('new_statement_form', clear_on_submit=True):
            new_statement_utterance = st.text_input('New Performance Statement', '', help='Paste your statement here.')
            add_statement = st.form_submit_button('Evaluate')

        manual_check = st.checkbox('Check before adding', value = False)

        # placeholder for where the manual check pane will be
        manual_check_pane = st.empty()

        # auxilary function to commit extraction, will be used more than once below
        def aux_commit_extraction():
            st.session_state['latest_insertions'] = engine.extracted_statement()
            engine.commit()

        #
        # EXTRACT: If we don't have extracted facts yet, let's try to do that.
        #
        if not engine.has_extracted_statement():
            if add_statement:
                engine.extract_statement(new_statement_utterance)

        #
        # COMMIT: If now we have the extracted statement, prepare to commit or commit them directly.
        #
        if engine.has_extracted_statement():

            # does the user want to manually check the extracted facts?
            if manual_check:

                with manual_check_pane.container():
                    accept = st.button('Accept Score')
                    cancel = st.button('Cancel Score')
                    st.write('Extracted facts:')
                    st.write(engine.extracted_statement())

                    if accept:
                        aux_commit_extraction()

                    elif cancel:
                        engine.cancel()
                        st.session_state['insertion_cancelled'] = True

            else: # no manual check needed, lets just commit
                aux_commit_extraction()

    ###################
    # Status messages #
    ###################

    if st.session_state['latest_insertions'] is not None:
        st.success(f'Added {st.session_state["latest_insertions"]} statements to the database.')
        st.session_state['latest_insertions'] = None
        manual_check_pane.empty()
    elif st.session_state['insertion_cancelled'] == True:
        st.info('Insertion cancelled.')
        st.session_state['insertion_cancelled'] = False
        manual_check_pane.empty()


if __name__ == '__main__':
    app()