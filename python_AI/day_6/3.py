from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
prompt = "AI서비스의 인상깊은 도형으로 이루어진 것 같은 심플하고 인상깊은 로고를 제작해줘"

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    n=1,
    response_format="b64_json"  # base64로 받기
)

image_base64 = response.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("generated_image1.png", "wb") as f:
    f.write(image_bytes)

print("이미지 생성 완료!")