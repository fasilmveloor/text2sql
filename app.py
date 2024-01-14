from dotenv import load_dotenv
load_dotenv() # loading all variables from .env

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# configure our API Key
genai.configure(api_key=os.getenv('API_KEY'))

# function to load gemini model and provide sql query as response
def get_gemini_response(question: str, prompt: str):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

## Function to retrieve query from the sql database
def read_sql_query(sql: str, db: str):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries.
    The sql database has the table with the name STUDENT and the columns are NAME, CLASS, SECTION, MARKS.
    \n
    Example 1 - How many entries are there present in the table?
    the sql command will be something like select count(*) from STUDENT;
    \n
    Example 2 - Tell me all the students studying in the 10th class?
    the sql command will be something like select * from STUDENT where CLASS = "10th";
    also the sql code should not have ``` in the beginning or end and sql word in output
    """
]

st.set_page_config(page_title="Retrieve any sql query")
st.header("Gemini app to retrieve sql Data")

## User Input
question = st.text_input("Input: ", key="input")
submit = st.button("Submit")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt[0])
    print(response)
    data = read_sql_query(response, 'sql.db')
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)
