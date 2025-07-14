import streamlit as st
import requests
from PIL import Image
import io

def avatar_tab():
    st.subheader("🧑‍🎨 Avatar Creator")

    file = st.file_uploader("Upload a selfie", type=["jpg", "png"])
    if file and st.button("Toonify"):
        res = requests.post(
            "https://hf.space/embed/deepghs/toonify/+/api/predict",
            json={"data": [f"data:image/jpeg;base64,{file.getvalue().decode('latin1')}"]}
        )
        try:
            output_url = res.json()['data'][0]
            st.image(output_url, caption="Toonified Avatar")
        except:
            st.error("Failed to create avatar.")
