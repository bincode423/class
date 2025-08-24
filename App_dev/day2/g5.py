import gradio as gr
import pyttsx3
import tempfile
import random
from datetime import datetime
from ollama import chat

def tts(text):
    if not text.strip():
        return None
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        temp_filename = temp_file.name
        temp_file.close()
        
        engine.save_to_file(text, temp_filename)
        engine.runAndWait()

        return temp_filename

    except Exception as e:
        print(f"Error: {e}")
        return None

chat_history = [{"role": "system", "content": "You are a helpful assistant."}]

def ollama_chat(text):
    chat_history.append({"role": "user", "content": f" ask : {text}"})
    stream = chat(
        model='exaone3.5:2.4b',
        messages=chat_history
    )
    chat_history.append({"role": "assistant", "content": stream.message.content})
    return stream.message.content


def ai_assistant(user_text):
    if user_text.strip() == None:
        return None, None
    user_text = user_text.lower()
    response = ollama_chat(user_text)
    return response, tts(response)

demo = gr.Interface(
    fn = ai_assistant,
    inputs = gr.Textbox(label="User Input"),
    outputs = [gr.Textbox(label="AI Assistant Response"),
               gr.Audio(label="Audio Output")],
    title = "AI Assistant",
    description = "Ask me anything",
)
demo.launch()