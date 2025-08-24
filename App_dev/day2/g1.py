import gradio as gr
from PIL import Image

def black_white_filter(image):
    if image == None:
        return None
    image = image.convert("L")
    image = image.convert("RGB")
    return image

demo = gr.Interface(
    fn=black_white_filter,
    inputs=gr.Image(type="pil", label="Input Image"),
    outputs=gr.Image(type="pil", label="Output Image"),
    title="Black and White Filter",
    description="Convert your image to black and white",
)

demo.launch()