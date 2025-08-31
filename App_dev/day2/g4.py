import gradio as gr
import pyttsx3
import io
import wave
import tempfile
import os

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

demo = gr.Interface(
    fn = tts,
    inputs = gr.Textbox(label="Text to convert to speech"),
    outputs = gr.Audio(label="Audio Output"),
    title = "Text to Speech",
    description = "Convert text to speech",
)
demo.launch()