import gradio as gr
from ollama import chat


# prompt = f'When I give you a keyword, return exactly {size} unique sub-keywords related to it, separated by spaces. Do not include any explanations or extra text. Match the language of the input keyword.'
# stream = chat(model="exaone3.5:7.8b", messages=[
#     {"role": "system", "content": prompt},
#     {"role": "user", "content": option}
# ], stream=True)

# rt = ''
# for chunk in stream:
#     rt += chunk.message.content
# new_keywords = set(rt.split())

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
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything"),
    outputs=gr.Textbox()
)
demo.launch()