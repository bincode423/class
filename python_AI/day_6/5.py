
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = "너는 파이썬 개발자야. 코딩에 관련된 질문에 친절하게 대답하지."

history = []
print("Gemini 챗봇이 시작되었습니다. 'quit'을 입력하면 종료됩니다.\n")

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = "너는 파이썬 개발자야. 코딩에 관련된 질문에 친절하게 대답하지."

history = []
print("Gemini 챗봇이 시작되었습니다. 'quit'을 입력하면 종료됩니다.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("대화를 종료합니다.")
        break

    history_text = ""
    for m in history:
        role = "사용자" if m["role"] == "user" else "AI"
        history_text += f"{role}: {m['content']}\n"

    contents = (
        f"[시스템]\n{SYSTEM_PROMPT}\n\n"
        f"[대화]\n{history_text}사용자: {user_input}\nAI:"
    )

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            temperature=0.7, 
        ),
    )

    answer = getattr(resp, "text", "") or "(빈 응답)"
    print("AI:", answer, "\n")

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": answer})
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = "너는 파이썬 개발자야. 코딩에 관련된 질문에 친절하게 대답하지."

history = []
print("Gemini 챗봇이 시작되었습니다. 'quit'을 입력하면 종료됩니다.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("대화를 종료합니다.")
        break

    history_text = ""
    for m in history:
        role = "사용자" if m["role"] == "user" else "AI"
        history_text += f"{role}: {m['content']}\n"

    contents = (
        f"[시스템]\n{SYSTEM_PROMPT}\n\n"
        f"[대화]\n{history_text}사용자: {user_input}\nAI:"
    )

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            temperature=0.7, 
        ),
    )

    answer = getattr(resp, "text", "") or "(빈 응답)"
    print("AI:", answer, "\n")

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": answer})
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = "너는 파이썬 개발자야. 코딩에 관련된 질문에 친절하게 대답하지."

history = []
print("Gemini 챗봇이 시작되었습니다. 'quit'을 입력하면 종료됩니다.\n")

while True:
    user_input = input("You: ")b
    if user_input.lower() in ["quit", "exit", "q"]:
        print("대화를 종료합니다.")
        break

    history_text = ""
    for m in history:
        role = "사용자" if m["role"] == "user" else "AI"
        history_text += f"{role}: {m['content']}\n"

    contents = (
        f"[시스템]\n{SYSTEM_PROMPT}\n\n"
        f"[대화]\n{history_text}사용자: {user_input}\nAI:"
    )

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            temperature=0.7, 
        ),
    )

    answer = getattr(resp, "text", "") or "(빈 응답)"
    print("AI:", answer, "\n")

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": answer})
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("대화를 종료합니다.")
        break

    history_text = ""
    for m in history:
        role = "사용자" if m["role"] == "user" else "AI"
        history_text += f"{role}: {m['content']}\n"

    contents = (
        f"[시스템]\n{SYSTEM_PROMPT}\n\n"
        f"[대화]\n{history_text}사용자: {user_input}\nAI:"
    )

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            temperature=0.7, 
        ),
    )

    answer = getattr(resp, "text", "") or "(빈 응답)"
    print("AI:", answer, "\n")

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": answer})