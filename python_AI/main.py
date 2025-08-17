import speech_recognition as sr
import wave

def record_and_save(filename: str, duration: int = 5, device_index: int = 1):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=device_index)

    with mic as source:
        print(f"{duration}초 동안 녹음 시작...")
        audio = r.listen(source, phrase_time_limit=duration)
        print("녹음 완료, 파일로 저장 중...")

    # audio.get_wav_data()는 bytes 타입, 이를 파일에 저장
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())

    print(f"'{filename}' 파일에 저장되었습니다.")

if __name__ == "__main__":
    record_and_save("output.wav", duration=5, device_index=1)







# from speech_recognition import *
# from ollama import chat
# import edge_tts
# import asyncio
# import pygame
# import time


# name = '히로'

# def stt(time):
#     r = Recognizer()
#     mic = Microphone()
#     with mic as source: 
#         audio= r.listen(source,phrase_time_limit=time)
#     try: return r.recognize_google(audio, language='ko')
#     except: return 'None'

# print(stt(10))


# # pygame.mixer.init()
# # def play_sound(file_path):
# #     pygame.mixer.music.load(file_path)
# #     pygame.mixer.music.play()
# #     while pygame.mixer.music.get_busy():
# #         time.sleep(0.1)
# #     pygame.mixer.music.stop()
# #     pygame.mixer.music.unload()

# # async def speak(text):
# #     communicate = edge_tts.Communicate(text=text, voice="ko-KR-SunHiNeural")
# #     await communicate.save("voice.mp3")


# # def tts(text):
# #     asyncio.run(speak(text))
# #     play_sound('voice.mp3')

# # tts('안녕하세요. 히로입니다.')
# # while True:
# #     text = stt(1)
# #     print(text)
# #     if '히로' in text:
# #         tts('안녕하세요.')
# #         text = stt(5)
# #         prompt = '너의 이름은 HIRO 야.'
# #         stream = chat(model="exaone3.5:7.8b", messages=[
# #             {"role": "system", "content": prompt},
# #             {"role": "user", "content": text}
# #         ], stream=True)
# #         for chunk in stream:
# #             tts(chunk.message.content)