import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import base64
import os

# --- Page Config ---
st.set_page_config(page_title="Translator", page_icon="🌐", layout="centered")

# --- Language Map ---
LANGUAGES = {
    'English': 'en', 'Tamil': 'ta', 'Hindi': 'hi', 'Spanish': 'es', 'French': 'fr',
    'German': 'de', 'Chinese': 'zh-CN', 'Japanese': 'ja', 'Korean': 'ko',
    'Arabic': 'ar', 'Portuguese': 'pt', 'Russian': 'ru', 'Italian': 'it'
}

# --- Header ---
st.markdown("## 🌐 Simple Translator")
st.markdown("Translate text between multiple languages easily.")

# --- Sidebar ---
st.sidebar.header("Settings")
source_lang = st.sidebar.selectbox("From", list(LANGUAGES.keys()), index=0)
target_lang = st.sidebar.selectbox("To", list(LANGUAGES.keys()), index=1)
auto_play = st.sidebar.checkbox("🔊 Auto-play translation audio", value=False)

# --- Input ---
text_input = st.text_area("Enter text to translate:", height=150)
if st.button("Translate"):
    if source_lang == target_lang:
        st.warning("Source and target languages must be different.")
    elif not text_input.strip():
        st.error("Please enter text to translate.")
    else:
        try:
            translated = GoogleTranslator(source=LANGUAGES[source_lang], target=LANGUAGES[target_lang]).translate(text_input)
            st.success("Translation complete!")

            st.markdown("### 📝 Translated Text")
            st.text_area("Translation", value=translated, height=150)

            # Audio Section
            def play_audio(text, lang_code):
                try:
                    tts = gTTS(text=text[:1000], lang=lang_code)
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
                        tts.save(tmp.name)
                        audio_bytes = open(tmp.name, "rb").read()
                        b64 = base64.b64encode(audio_bytes).decode()
                        audio_html = f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
                        st.markdown(audio_html, unsafe_allow_html=True)
                        os.unlink(tmp.name)
                except Exception as e:
                    st.error(f"Audio error: {e}")

            st.markdown("### 🔊 Audio")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔈 Original"):
                    play_audio(text_input, LANGUAGES[source_lang])
            with col2:
                if st.button("🔈 Translation") or auto_play:
                    play_audio(translated, LANGUAGES[target_lang])
        except Exception as e:
            st.error(f"Translation error: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Built with Streamlit & Deep Translator • v1.0")

