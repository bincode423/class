import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Game point check",
    page_icon="⚙️",
    layout="wide"
)

st.title("Game point checker")
st.write("친구들과 게임 점수를 공유하고 순위를 확인해보세요!")

if "scores" not in st.session_state:
    st.session_state.scores = {}

if "game_history" not in st.session_state:
    st.session_state.game_history = []

st.sidebar.header("Players")
new_player = st.sidebar.text_input("New player name")

if st.sidebar.button("Add Player"):
    if new_player and new_player not in st.session_state.scores:
        st.session_state.scores[new_player] = 0
        st.sidebar.success(f"{new_player} 추가되었습니다.")
    else:
        st.sidebar.error(f"{new_player} 이미 존재하거나 이름을 입력하시지 않았습니다.")

st.header("Score Board")
if st.session_state.scores:
    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ranking")
        for i, (player, score) in enumerate(sorted_scores, start=1):
            if i <= 3:
                st.success(f"###### {i}위 {player}님 {score}점")
            elif i <= 10:
                st.info(f"###### {i}위 {player}님 {score}점")
            elif i <= 20:
                st.warning(f"###### {i}위 {player}님 {score}점")
            else:
                st.error(f"###### {i}위 {player}님 {score}점")
    with col2:
        st.subheader("Add score")
        selected_player = st.selectbox("Select a player", list(st.session_state.scores.keys()))
        point_to_add = st.number_input("Add score", min_value=-100, max_value=100, value=0)
        if st.button("Add score"):
            old_score = st.session_state.scores[selected_player]
            st.session_state.scores[selected_player] += point_to_add
            new_score = st.session_state.scores[selected_player]

            st.session_state.game_history.append(
                {'player': selected_player,
                 'point': point_to_add, 
                 'total': new_score,
                 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            st.success(f"{selected_player}님 {point_to_add}점 추가되었습니다.")
            st.rerun()
else:
    st.write("No players added yet.")

if st.session_state.scores:
    if st.button("Reset all scores", use_container_width=True):
        st.session_state.scores = {}
        st.session_state.game_history = []
        st.success("모든 점수가 초기화되었습니다.")
        st.rerun()

if st.session_state.game_history:
    st.header("Game History")
    recent_history = st.session_state.game_history[-5:]

    for record in reversed(recent_history):
        cols = st.columns([1,2,1,1])
        with cols[0]:
            st.write(record['date'])
        with cols[1]:
            st.write(record['player'])
        with cols[2]:
            if record['point'] > 0:
                st.success(f"+{record['point']}")
            elif record['point'] < 0:
                st.error(f"{record['point']}")
        with cols[3]:
            st.write(record['total'])

if st.session_state.scores:
    st.header("Game chart")
    col1, col2, col3 = st.columns(3)
    with col1:
        total_players = len(st.session_state.scores)
        st.metric(f"Total players",total_players)
    with col2:
        average_score = sum(st.session_state.scores.values()) / total_players
        st.metric(f"Average score",f"{average_score:.2f}")
    with col3:
        if st.session_state.scores:
            max_score = max(st.session_state.scores.values())
            st.metric(f"Max score",max_score)

st.sidebar.header("game settings")
target_score = st.sidebar.number_input("Target score", min_value=50, max_value=200, value=100, step=1)

if st.session_state.scores:
    high_score = max(st.session_state.scores.values())

    if high_score >= target_score:
        winner_name = ""
        for player, score in st.session_state.scores.items():
            if score == high_score:
                winner_name = player
                break
    st.balloons()
    st.success(f"{winner_name}님이 {target_score}점을 달성했습니다! 축하합니다.")