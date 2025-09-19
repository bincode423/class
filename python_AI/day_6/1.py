from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

def load_model():
    model_name = "skt/kogpt2-base-v2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

if 'model' not in st.session_state:
    st.session_state.tokenizer, st.session_state.model = load_model()

def generate_text(prompt, max_len=40):
    inputs = st.session_state.tokenizer(prompt, return_tensors="pt")
    outputs = st.session_state.model.generate(**inputs, max_length=max_len, do_sample=True, top_p=0.9, temperature=0.8)
    return st.session_state.tokenizer.decode(outputs[0], skip_special_tokens=True)

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