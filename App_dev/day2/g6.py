import gradio as gr
import random
from datetime import datetime

def home_page():
    return "홈페이지"

def greeting_page(name):
    return f"안녕하세요, {name}님!"

home_tab = gr.Interface(
    fn = home_page,
    inputs = None,
    outputs = gr.Markdown(),
    title = '홈',
    description = '홈페이지',
)
greeting_tab = gr.Interface(
    fn = greeting_page,
    inputs = gr.Textbox(),
    outputs = gr.Textbox(),
    title = '인사말',
    description = '인사말 페이지',
)

demo = gr.TabbedInterface(
    [home_tab, greeting_tab],
    ["홈","인사말"],
    title = '나만의 웹앱')
demo.launch()