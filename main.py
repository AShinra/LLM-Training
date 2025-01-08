import streamlit as st
from langchain.llms import OpenAI
from file_uploader import upload_xlsx_file
from pre_process import get_headers
import pandas as pd
import openpyxl
import os

# Defining a function to generate a response using the OpenAI model
def generate_response(input_text):
    # Initializing the OpenAI model with a specified temperature and API key
    llm = OpenAI(temperature=0.5, openai_api_key=openai_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
    # st.write(llm(input_text))
    return llm(input_text)

def api_prompt():
    text = f'''Role: You are tasked to create a summary from the given article based on the following criteria
    
                "Read the following story or article carefully. Summarize it in a detailed and structured way, highlighting the key points, main events, and core themes. Ensure the summary captures:

                1. The central idea or main argument.
                2. Important supporting details, including relevant facts, figures, and examples.
                3. Any significant quotes or dialogue that add value to the story.
                4. The overall tone and purpose of the article.
                5. Key takeaways or lessons (if applicable).
                
                Make the summary clear and concise, while preserving the essence of the original content. Structure it in complete paragraphs, with transitions that ensure smooth readability."'''
    return text

client = 'Manulife'

# Setting the title of the Streamlit application
st.title('Article Summarizer 🤖')

# get the API KEY
openai_api_key = st.secrets["openai"]

# get the uploaded file
uploaded_file = upload_xlsx_file()

if uploaded_file is not None:

    df, headers = get_headers(uploaded_file)

    if headers is not None:
        col1, col2, col3 = st.columns(3)
        with col1:
            selected_column = st.selectbox(label='Select Column to Summarize', options=headers)
            if st.button('Submit'):
                
                _path = os.getcwd()
                _file = f'{_path}/summarized_sample.xlsx'
                wb = openpyxl.Workbook(_file)
                wb.save(_file)
                wb.close()

                df['Summary'] = ''
                for i in df.index:
                    content_to_summarize = df.loc[i, selected_column]
                    df.loc[i, 'Summary'] = generate_response(f'{api_prompt()}\n\n{content_to_summarize}')
                
                st.dataframe(df)
                writer = pd.ExcelWriter(_file, engine='openpyxl', mode='a')
                df.to_excel(writer, sheet_name='CLEANED', index=False)
                writer.close()

                result_file = open(_file, 'rb')
                st.success(f':red[NOTE:] Downloaded file will go to the :red[Downloads Folder]')
                st.download_button(label='📥 Download Excel File', data= result_file, file_name= f'summarized.xlsx')   







                    # Creating a form in the Streamlit app for user input
                    # with st.form('my_form'):
                        # Adding a text area for user input with a default prompt
                        # text = st.text_area('Enter text:', '')
                        # Adding a submit button for the form
                        # submitted = st.form_submit_button('Submit')
                        # Displaying a warning if the entered API key does not start with 'sk-'
                        # if not openai_api_key.startswith('sk-'):
                        #     st.warning('Please enter your OpenAI API key!', icon='⚠')
                        # If the form is submitted and the API key is valid, generate a response
                        # if submitted and openai_api_key.startswith('sk-'):
                            # generate_response(f'{api_prompt()}\n\n{content_to_summarize}')
