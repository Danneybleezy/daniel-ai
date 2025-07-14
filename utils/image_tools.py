import streamlit as st
import requests
from PIL import Image
import io

def enhance_tab():
    st.subheader("🖼️ Enhance Face (GFPGAN)")

    file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if file and st.button("✨ Enhance"):
        img_bytes = file.read()
        res = requests.post(
            "https://api-inference.huggingface.co/models/akhaliq/Real-ESRGAN",
            headers={"Authorization": "Bearer hf_your_huggingface_token"},  # Optional for higher speed
            data=img_bytes
        )
        if res.status_code == 200:
            image = Image.open(io.BytesIO(res.content))
            st.image(image, caption="Enhanced")
        else:
            st.error("Enhancement failed.")

def generate_image_tab():
    st.subheader("🎨 Generate Image")

    prompt = st.text_input("Enter prompt:", placeholder="A tiger riding a motorcycle")
    if prompt and st.button("Generate"):
        with st.spinner("Generating..."):
            res = requests.post(
                "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
                headers={"Authorization": "Bearer hf_your_huggingface_token"},
                json={"inputs": prompt}
            )
            if res.status_code == 200:
                image = Image.open(io.BytesIO(res.content))
                st.image(image)
            else:
                st.error("Image generation failed.")
