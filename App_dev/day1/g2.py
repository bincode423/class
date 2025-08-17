import gradio as gr
import random

def compliment_hello(name):
    compliments = [
        "오늘도 멋지게 잘 해내고 있어요!",
        "너무 멋지게 잘 해내고 있어요!",
        "당신은 항상 잘 하고 있어요!",
        "당신도 무엇이든지 할 수 있어요",
        "당신은 정말 대단해요."
    ]

    if name == '':
        return "이름을 입력하세요."
    else:
        return f"{name}님, {random.choice(compliments)}"
    
demo = gr.Interface(
    fn=compliment_hello,
    inputs=gr.Textbox(label="이름을 입력하세요."),
    outputs= 'text'
)
demo.launch()