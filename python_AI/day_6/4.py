from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="너는 파이썬 개발자야. 코딩에 관련된 질문에 친절하게 대답하지. 자기소개하고 무엇을 도와줄 지 질문해.",),
    contents="파이썬에서 리스트와 튜플의 차이점은 무엇인가?"
)

print(response.text)