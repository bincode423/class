import random
import streamlit as st
import gensim.downloader as api

KO2EN = {
    "강아지":"dog","개":"dog","고양이":"cat","곰":"bear","호랑이":"tiger","사자":"lion",
    "코끼리":"elephant","말":"horse","늑대":"wolf","여우":"fox","토끼":"rabbit","사슴":"deer",
    "원숭이":"monkey","침팬지":"chimpanzee","고릴라":"gorilla","판다":"panda","소":"cow",
    "돼지":"pig","양":"sheep","염소":"goat","닭":"chicken","독수리":"eagle","오리":"duck"
}
MAX_TURNS = 7

@st.cache_resource(show_spinner=True)
def load_model():
    st.write("임베딩 모델 로딩 중... (최초 1회)")
    model = api.load("glove-wiki-gigaword-50")
    return model

model = load_model()
vocab = set(model.key_to_index.keys())
ANIMALS_KO = [ko for ko, en in KO2EN.items() if en in vocab]

if "answer_ko" not in st.session_state:
    st.session_state.answer_ko = random.choice(ANIMALS_KO)
    st.session_state.answer_en = KO2EN[st.session_state.answer_ko]
    st.session_state.turns = 0
    st.session_state.history = []  # [(guess_ko, sim_float)]
    st.session_state.done = False
    st.session_state.result_msg = ""

def new_game():
    st.session_state.answer_ko = random.choice(ANIMALS_KO)
    st.session_state.answer_en = KO2EN[st.session_state.answer_ko]
    st.session_state.turns = 0
    st.session_state.history = []
    st.session_state.done = False
    st.session_state.result_msg = ""

st.title("🐾 동물 유사도 퀴즈")
st.caption("아래 한글 동물 버튼을 선택하면 의미 유사도를 확인해 맞히는 게임")

st.write("**후보 동물 버튼:**")

cols = st.columns(3)
for i, ko in enumerate(ANIMALS_KO):
    if cols[i % 3].button(ko):
        if not st.session_state.done:
            st.session_state.turns += 1
            if ko == st.session_state.answer_ko:
                st.session_state.done = True
                st.session_state.result_msg = f"🎉 정답! **{st.session_state.answer_ko}**"
                st.balloons()
            else:
                guess_en = KO2EN[ko]
                sim = float(model.similarity(guess_en, st.session_state.answer_en))
                st.session_state.history.append((ko, sim))
                if st.session_state.turns >= MAX_TURNS:
                    st.session_state.done = True
                    st.session_state.result_msg = f"❌ 실패! 정답은 **{st.session_state.answer_ko}**"

st.button("새 게임 시작", on_click=new_game)


left = MAX_TURNS - st.session_state.turns
st.write("---")
st.subheader("진행 상황")
st.write(f"남은 시도: **{max(0,left)} / {MAX_TURNS}**")

if st.session_state.history:
    st.write("**시도 기록 (최근 순)**")
    for g, s in reversed(st.session_state.history):
        st.write(f"- {g} → 유사도: **{s:.3f}**")

if st.session_state.done and st.session_state.result_msg:
    st.success(st.session_state.result_msg)