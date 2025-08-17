import gradio as gr
from ollama import chat
import random

def smart_hello(name):
    if name == '':
        return "이름을 입력하세요."
    else:
        return f"안녕하세요, {name}님!"

demo = gr.Interface(
    fn=smart_hello,
    inputs=gr.Textbox(label="이름을 입력하세요."),
    outputs= 'text'
)
demo.launch()