import streamlit as st
from chat_app import FilmSearch
import pandas as pd
import json
import os

from dotenv import load_dotenv
load_dotenv()




st.set_page_config(
    page_title="Movie Explorer",
    page_icon="🎥",
)
 
openai_api_key = os.environ["OPENAI_API_KEY"]

with open('./config.json') as f:
    config = json.load(f)

st.markdown("<h1 style='text-align: center;'>🎬 Movie Explorer</h1>",
            unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Unlock the cinematic universe with ease..</h2>",
            unsafe_allow_html=True)

beginning_year = config["years"][0]
ending_year = config["years"][-1]

f"""
 This movie exploration bot has access to a curated database featuring approximately the top 100 films spanning from {beginning_year}-{ending_year}. Discover hidden gems, timeless classics, and blockbuster hits—all at your fingertips
"""

 


def generate_response(input_text, openai_api_key):
    pinecone_api_key = os.environ["PINECONE_API_KEY"]
    pinecone_index_name = os.environ["PINECONE_INDEX_NAME"]

    chat = FilmSearch(openai_api_key, pinecone_api_key, pinecone_index_name)
    st.write_stream(chat.ask(input_text))


st.markdown(
    "*Feel free to try one of these sample queries, or type your own below.*")

col1, col2, col3 = st.columns(3)

with col1:
    example = "I'm looking for a sci-fi comedy movies."
    if st.button(example, key='button1'):
        st.session_state.query = example

with col2:
    example = "Recommend some funny zombie movies ."
    if st.button(example, key='button2'):
        st.session_state.query = example

with col3:
    example = "Can you suggest a family-friendly movie?."
    if st.button(example, key='button3'):
        st.session_state.query = example

with st.form('my_form'):
    text = st.text_area(
        label='Query:',
        placeholder='Type your query here.',
        value=st.session_state.query if 'query' in st.session_state else '',
        label_visibility='hidden')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    if submitted:
        generate_response(text, openai_api_key=openai_api_key)

st.divider()

