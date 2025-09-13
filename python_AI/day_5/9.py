import streamlit as st

st.title("Streamlit 시작")
st.write("안녕하세요! 첫 번째 예제입니다.")

number = st.number_input("숫자를 입력하세요", min_value=0, max_value=100, value=10)

if st.button("두 배로 계산하기"):
    st.write(f"결과: {number * 2}")

name = st.text_input("이름을 입력하세요", "")
if name:
    st.write(f"반가워요, **{name}** 님!")