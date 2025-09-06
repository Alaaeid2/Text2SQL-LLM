import streamlit as st
import os
import sqlite3

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv      

load_dotenv()


def get_sql_query(user_query):
    groq_sys_prompt = ChatPromptTemplate.from_template("""
                    You are an expert in converting English questions to SQL query!
                    The SQL database has the name students and has the following columns - NAME, AGE, GENDER, COURSE, 
                    SECTION and MARKS. For example, 
                    Example 1 - How many entries of records are present?, 
                        the SQL command will be something like this SELECT COUNT(*) FROM students;
                    Example 2 - Tell me all the students studying in Data Science COURSE?, 
                        the SQL command will be something like this SELECT * FROM students 
                        where COURSE="Data Science"; 
                    also the sql code should not have ``` in beginning or end and sql word in output.
                    Now convert the following question in English to a valid SQL Query: {user_query}. 
                    No preamble, only valid SQL please
                                                       """)
        
    model="llama-3.3-70b-versatile"
    llm = ChatGroq(
        model= model,
        groq_api_key= os.environ.get("GROQ_API_KEY"),

    )
    chain= groq_sys_prompt | llm | StrOutputParser()
    response = chain.invoke({"user_query": user_query})
    
    return response

def get_data_from_database(sql_query):
    database = "student.db"
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        data = cursor.execute(sql_query).fetchall()
        return data



def main():
    st.set_page_config(page_title="Text to SQL with LLM", layout="wide")
    st.header("Talk to your Database")
    st.write("This is a simple Streamlit app to convert text to SQL using LLM.")

    user_query = st.text_input("Enter your query here:")
    submit_btn = st.button("Enter")
    if submit_btn:
        sql_query = get_sql_query(user_query)
        retrieved_data = get_data_from_database(sql_query)
        st.header("Hi, I am your Database Assistant")
        st.subheader(f"Retrieving results from the database for the query: [{sql_query}]")
        for row in retrieved_data:
            st.header(row)

if __name__ == "__main__":
    main()