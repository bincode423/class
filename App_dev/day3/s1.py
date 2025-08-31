import streamlit as st

#title
st.title("Streamlit")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a text")

#text
st.write("This is a write")
st.text("This is a text")
st.markdown("This is a markdown")

#user input
name = st.text_input("Enter your name")
age = st.number_input("Enter your age",min_value=0,max_value=100,value=20)
hobby = st.selectbox("Select your hobby",["reading","swimming","coding"])

#if statement
if st.button("Submit"):
    st.write(f"Hello {name}! You are {age} years old and your hobby is {hobby}")

#sidebar
st.sidebar.title("Sidebar")
option = st.sidebar.selectbox("Select an option",["home","about","contact"])

#devide
col1, col2 = st.columns(2)
with col1:
    st.write("This is a column 1")
with col2:
    st.write("This is a column 2")

#extend
with st.expander("Expand me"):
    st.write("This is a expander")


#progress bar
progress = st.progress(0.5)
status = st.empty()