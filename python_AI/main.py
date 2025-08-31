from speech_recognition import *
from ollama import chat
import edge_tts
import asyncio
import pygame
import time


name = '히로'
prompt = "Your name is HIRO AI. Your company is HIRO AI."
    

pygame.mixer.init()
def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

async def speak(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice="ko-KR-InJoonNeural",
        rate='+40%',
        volume='+0%'
    )
    await communicate.save("voice.mp3")

def tts(text):
    asyncio.run(speak(text))
    play_sound('voice.mp3')

tts('안녕하세요, 저는 당신의 AI비서 히로입니다. 함꼐 작업할 마음에 가슴이 뛰는 것 같아요!')
chat_history = [{"role": "system", "content": prompt}]
while True:
    ipt = input('사용자 >> ')
    chat_history.append({"role": "user", "content": ipt})
    stream = chat(
        model="exaone3.5:7.8b", 
        messages=chat_history,
        stream=True)
    rt = ''
    print('히로 >> ', end='', flush=True)
    for chunk in stream:
        ck = chunk.message.content
        print(ck, end='', flush=True)
        rt += ck
    tts(rt.replace('HIRO', '히로'))
    print()
    chat_history.append({"role": "assistant", "content": rt})