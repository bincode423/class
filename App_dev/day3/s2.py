import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Seunghyun Bin",
                   page_icon=":tada:",
                   layout="wide")

st.title("Seunghyun Bin")

now = datetime.now()
st.write(f"Now: {now.strftime("%Y-%m-%d %H:%M")}")

st.header("Hi, I'm Seunghyun Bin")
st.write("I'm a student in Korea.")

btn = st.button("Say hello")
if btn:
    st.write("Thank you for clicking the button")
    st.balloons()