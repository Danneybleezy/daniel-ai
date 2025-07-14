import streamlit as st
import pytesseract
from PIL import Image
import requests

def diagram_tab(groq_key):
    st.subheader("🧑‍🏫 Upload a diagram or chart")

    file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if file and st.button("🧠 Explain Diagram"):
        img = Image.open(file)
        st.image(img, caption="Uploaded Diagram")

        text = pytesseract.image_to_string(img)
        st.text_area("Extracted Text", text, height=200)

        headers = {
            "Authorization": f"Bearer {groq_key}",
            "Content-Type": "application/json"
        }
        body = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "Explain this diagram:"},
                {"role": "user", "content": text}
            ]
        }
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
        explanation = res.json()["choices"][0]["message"]["content"]
        st.success(explanation)
