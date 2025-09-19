from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

if 'client' not in st.session_state:
    load_dotenv()
    st.session_state.client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def generate_text(input):
    response = st.session_state.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=input
    )
    return response.text

if 'history' not in st.session_state:
    st.session_state.history = []

for now in st.session_state.history:
    if now['content'] == 'user':
        with st.chat_message("user"):
            st.write(now['message'])
    else:
        with st.chat_message("assistant"):
            st.write(now['message'])

prompt = st.chat_input("Say something")
if prompt:
    st.session_state.history.append({'content':'user', 'message':prompt})
    with st.chat_message("user"):
        st.write(prompt)
    ai = generate_text(prompt)
    with st.chat_message("assistant"):
        st.write(ai)
    st.session_state.history.append({'content':'ai', 'message':ai})