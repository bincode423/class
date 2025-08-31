import gradio as gr
from ollama import chat

def daily_fortune(name, sign):
    yield ["🔮 운세를 생성중입니다...", "🎨 행운의 색을 준비중입니다..."]

    prompt = "너는 사용자의 별자리가 주어지면 오늘의 운세만 반환해야 해. 긍정, 부정적인 것 모두 만들어내야 해."
    stream = chat(model="exaone3.5:7.8b", messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"이름 : {name}, 별자리 : {sign}"}
    ], stream=True)

    fortune = ""
    for chunk in stream:
        fortune += chunk["message"]["content"]
    yield [fortune, "🎨 행운의 색을 준비중입니다..."]

    prompt = "너는 사용자의 이름이 주어지면 특이한 색도 좋아. 오늘의 행운의 색을 알려줘야 해."
    stream = chat(model="exaone3.5:7.8b", messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"이름 : {name}"}
    ], stream=True)

    color = ""
    for chunk in stream:
        color += chunk["message"]["content"]

    yield [fortune, color]

star_signs = [
    '양자리 (Aries) : 3월 21일 ~ 4월 19일',
    '황소자리 (Taurus) : 4월 20일 ~ 5월 20일',
    '쌍둥이자리 (Gemini) : 5월 21일 ~ 6월 21일',
    '게자리 (Cancer) : 6월 22일 ~ 7월 22일',
    '사자자리 (Leo) : 7월 23일 ~ 8월 22일',
    '처녀자리 (Virgo) : 8월 23일 ~ 9월 22일',
    '천칭자리 (Libra) : 9월 23일 ~ 10월 22일',
    '전갈자리 (Scorpio) : 10월 23일 ~ 11월 22일',
    '궁수자리 (Sagittarius) : 11월 23일 ~ 12월 21일',
    '염소자리 (Capricorn) : 12월 22일 ~ 1월 19일',
    '물병자리 (Aquarius) : 1월 20일 ~ 2월 18일',
    '물고기자리 (Pisces) : 2월 19일 ~ 3월 20일'
]


with gr.Blocks(css=".generating {display: none !important;}") as demo:
    name = gr.Textbox(label="이름")
    sign = gr.Dropdown(label="별자리", choices=star_signs)
    fortune = gr.Markdown(label="운세")
    color = gr.Markdown(label="행운의 색")
    btn = gr.Button("운세 보기")
    btn.click(daily_fortune, inputs=[name, sign], outputs=[fortune, color])

demo.launch()