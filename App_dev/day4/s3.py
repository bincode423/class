import streamlit as st

st.set_page_config(page_title="할 일 관리",
                    page_icon=":memo:",
                    layout="wide")

st.title("할 일 관리")
st.write("오늘 해야 할 일들을 정리해봅시다.")
if "todo_list" not in st.session_state:
    st.session_state.todo_list = {}

new_todo = st.text_input("할 일을 입력하세요.")

if st.button("할 일 추가"):
    if new_todo:
        st.session_state.todo_list[new_todo] = False
        st.success(f"{new_todo} 추가되었습니다.")
        st.rerun()
    else:
        st.error("할 일을 입력하세요.")

st.header("할 일 목록")
if st.session_state.todo_list:
    st.write(f"총 {len(st.session_state.todo_list)}개의 할 일이 있습니다.")
    for i, todo in enumerate(st.session_state.todo_list.keys(), start=1):
        st.session_state.todo_list[todo] =  st.checkbox(f"##### {i}. {todo}", value=st.session_state.todo_list[todo])
else:
    st.error("할 일이 없습니다.")

if st.session_state.todo_list:
    if st.button("전체 삭제", use_container_width=True):
        st.session_state.todo_list = []
        st.success("모든 할 일이 삭제되었습니다.")
        st.rerun()