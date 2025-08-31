import gradio as gr
from PIL import Image,ImageEnhance

def rainbow_rotate_filter(image, ratation_angle, color_boost):
    if image == None:
        return None
    image = image.rotate(ratation_angle, expand=True, fillcolor=(255,255,255))
    
    image = ImageEnhance.Color(image)
    image = image.enhance(color_boost)

    image = ImageEnhance.Color(image)
    image = image.enhance(1.5)

    return image

demo = gr.Interface(
    fn=rainbow_rotate_filter,
    inputs=[gr.Image(type="pil", label="Input Image"),
            gr.Slider(0, 360, value=0, step=1, label="Rotate Angle"),
            gr.Slider(0, 3, value=1, step=0.1, label="Color Boost")],
    outputs=gr.Image(type="pil", label="Output Image"),
    title="Rainbow Rotate Filter",
    description="Rotate your image and boost the color",
)
demo.launch()