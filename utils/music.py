import streamlit as st

def music_tab():
    st.subheader("🎵 Music Generator")
    st.info("Experimental. Uses pre-generated samples.")

    music_options = {
        "Lofi Beat": "https://cdn.pixabay.com/audio/2023/05/10/audio_2481e79106.mp3",
        "Chill Piano": "https://cdn.pixabay.com/audio/2022/10/27/audio_82e3c1cd60.mp3"
    }

    choice = st.selectbox("Choose sample:", list(music_options.keys()))

    if choice:
        st.audio(music_options[choice], format="audio/mp3", autoplay=True)
