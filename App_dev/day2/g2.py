import gradio as gr
from PIL import Image,ImageEnhance

def brightness_filter(image, brightness):
    if image == None:
        return None
    image = ImageEnhance.Brightness(image).enhance(brightness)
    return image

demo = gr.Interface(
    fn=brightness_filter,
    inputs=[gr.Image(type="pil", label="Input Image"), gr.Slider(0, 3, value=1, step=0.1, label="Brightness")],
    outputs=gr.Image(type="pil", label="Output Image"),
    title="Brightness Filter",
    description="Adjust the brightness of your image",
)
demo.launch()