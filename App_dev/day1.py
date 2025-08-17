import gradio as gr
from ollama import chat

# def answer(Question):
#     prompt = "Your name is HIRO AI. Your company is HIRO AI."
#     stream = chat(model="exaone3.5:7.8b", messages=[
#         {"role": "system", "content": prompt},
#         {"role": "user", "content": Question}
#     ], stream=True)
#     rt = ''
#     for chunk in stream:
#         rt += chunk.message.content
#     return rt

def smart_hello(name):
    if name == '':
        return "이름을 입력하세요."
    else:
        return f"안녕하세요, {name}님!"

demo = gr.Interface(
    fn=smart_hello,
    inputs=gr.Textbox(lines=2, placeholder="이름을 입력하세요."),
    outputs=gr.Textbox()
)
demo.launch()

