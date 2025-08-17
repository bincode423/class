import gradio as gr

def cal(num1, operator, num2):
    if operator == '더하기':
        return num1 + num2
    elif operator == '빼기':
        return num1 - num2
    elif operator == '곱하기':
        return num1 * num2
    elif operator == '나누기':
        if num2 == 0:
            return '0으로 나눌 수 없습니다.'
        return num1 / num2
    elif operator == '몫':
        if num2 == 0:
            return '0으로 나눌 수 없습니다.'
        return num1 // num2
    elif operator == '나머지':
        if num2 == 0:
            return '0으로 나눌 수 없습니다.'
        return num1 % num2
demo = gr.Interface(
    fn = cal,
    inputs = [
        gr.Number(label = '숫자1'),
        gr.Dropdown(label = '연산자', choices = ['더하기', '빼기', '곱하기', '나누기','몫', '나머지']),
        gr.Number(label = '숫자2')
    ],
    outputs = 'text',
    title = 'Simple Calculator',
    description = 'This is a simple calculator that can add, subtract, multiply, and divide numbers.'
)
demo.launch()