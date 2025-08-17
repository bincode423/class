import gradio as gr

def age_calculator(birth_year):
    if birth_year == '':
        return '출생년도를 입력하세요.'
    elif birth_year > 2025:
        return '출생년도가 미래입니다.'
    current_year = 2025
    age = current_year - birth_year
    if age <= 19:
        return '청소년입니다.'
    else:
        return '성인입니다.'

demo = gr.Interface(
    fn = age_calculator,
    inputs = gr.Number(label = '출생년도', value = 2000),
    outputs = 'text',
    title = 'Age Calculator',
    description = '이것은 출생년도를 입력하면 청소년인지 성인인지 알려주는 계산기입니다.'
)
demo.launch()