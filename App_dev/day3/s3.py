import streamlit as st

st.sidebar.title("Sidebar")

name = st.sidebar.text_input("이름")
age = st.sidebar.number_input("나이", min_value=0, max_value=100, value=20)

grade = st.sidebar.selectbox("학점", ["A", "B", "C", "D", "F"])

hobby = st.sidebar.multiselect("취미", ["책읽기", "영화보기", "운동", "음악듣기"])

mood = st.sidebar.slider("기분", min_value=1, max_value=10, value=5)

if name:
    st.header(f"Hello {name}!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("basic info")
        st.write(f"age: {age}")
        st.write(f"grade: {grade}")

        if mood > 8:
            mood_emoji = "😍"
            mood_text = "very good"
        elif mood > 6:
            mood_emoji = "😊"
            mood_text = "good"
        elif mood > 4:
            mood_emoji = "😐"
            mood_text = "soso"
        elif mood > 2:
            mood_emoji = "😕"
            mood_text = "bad"
        else:
            mood_emoji = "😢"
            mood_text = "very bad"
        
        st.write(f"mood: {mood_emoji} {mood_text}")

    with col2:
        st.subheader("hobby")
        if hobby:
            for h in hobby:
                st.write(f"{h}")
        else:
            st.write("no hobby")
    
    if mood > 7:
        st.success("You are doing great!")
    elif mood >= 5:
        st.info("You are doing good!")
    else:
        st.error("Cheer up!")