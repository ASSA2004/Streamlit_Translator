import streamlit as st
from googletrans import Translator

# Page config
st.set_page_config(
    page_title="Language Translator v1",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Language Translator - Version 1")
st.markdown("*Basic text translation between English and Tamil*")

# Initialize translator
@st.cache_resource
def get_translator():
    return Translator()

translator = get_translator()

# Basic translation function
def translate_text(text, source_lang, target_lang):
    try:
        result = translator.translate(text, src=source_lang, dest=target_lang)
        return result.text
    except Exception as e:
        st.error(f"Translation error: {e}")
        return None

# Main interface
col1, col2 = st.columns(2)

with col1:
    st.header("📝 Input")
    
    # Language selection
    source_language = st.selectbox(
        "Source Language:",
        ["English", "Tamil"]
    )
    
    # Text input
    text_input = st.text_area(
        f"Enter your {source_language} text:",
        height=150,
        placeholder=f"Type your {source_language} text here..."
    )

with col2:
    st.header("🔄 Translation")
    
    # Determine target language
    target_language = "Tamil" if source_language == "English" else "English"
    source_lang = 'en' if source_language == 'English' else 'ta'
    target_lang = 'ta' if source_language == 'English' else 'en'
    
    st.write(f"**Target Language:** {target_language}")
    
    if text_input and text_input.strip():
        if st.button("🔄 Translate", type="primary"):
            with st.spinner("Translating..."):
                translated_text = translate_text(text_input, source_lang, target_lang)
                
                if translated_text:
                    st.subheader("📄 Results")
                    
                    # Original text
                    st.write("**Original:**")
                    st.info(text_input)
                    
                    # Translated text
                    st.write(f"**Translated ({target_language}):**")
                    st.success(translated_text)
    else:
        st.info("👆 Please enter some text to translate")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit & Google Translate*")