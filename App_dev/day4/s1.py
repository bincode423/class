import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0


if st.button("클릭"):
    st.session_state.count += 1

st.write(f"클릭 횟수: {st.session_state.count}")