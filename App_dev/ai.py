import gradio as gr
from ollama import chat
import random

def answer(Question):
    prompt = "Your name is HIRO AI. Your company is HIRO AI."
    stream = chat(model="exaone3.5:7.8b", messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": Question}
    ], stream=True)
    rt = ''
    for chunk in stream:
        rt += chunk.message.content
    return rt

demo = gr.Interface(
    fn=answer,
    inputs=gr.Textbox(label="질문을 입력하세요."),
    outputs= 'text'
)
demo.launch()