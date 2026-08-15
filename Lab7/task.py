import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO
import easyocr
from PIL import Image
import numpy as np
import torch


st.set_page_config(
    page_title="Multilingual News Summarizer",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Multilingual News Summarizer")

st.write(
    "Upload a screenshot or article image to extract text, "
    "summarize it, translate it into Nepali, and generate speech."
)


@st.cache_resource
def load_ocr():
    return easyocr.Reader(["en"], gpu=False)

reader = load_ocr()

@st.cache_resource
def load_summarization_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model
tokenizer, model = load_summarization_model()

def summarize_text(text):
    # Limit input length
    text = text[:5000]

    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )
    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=100,
            min_length=30,
            num_beams=4,
            early_stopping=True
        )
    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )
    return summary

uploaded_file = st.file_uploader(
    "Upload a screenshot or article image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )
    with st.spinner("🔍 Extracting text from image..."):
        image_array = np.array(image)
        results = reader.readtext(image_array)
        extracted_text = " ".join(
            result[1]
            for result in results
        )
    st.subheader("📄 Extracted Text")
    if extracted_text.strip():
        st.text_area(
            "OCR Result",
            extracted_text,
            height=200
        )
        if st.button("✨ Summarize Article"):
            with st.spinner("🧠 Generating summary..."):
                summary = summarize_text(
                    extracted_text
                )
            st.subheader("🇬🇧 English Summary")
            st.write(summary)
            with st.spinner("🌐 Translating to Nepali..."):
                translated = GoogleTranslator(
                    source="en",
                    target="ne"
                ).translate(summary)
            st.subheader("🇳🇵 Nepali Translation")
            st.write(translated)
            with st.spinner("🔊 Generating Nepali speech..."):
                tts = gTTS(
                    text=translated,
                    lang="ne"
                )
                mp3_bytes = BytesIO()
                tts.write_to_fp(mp3_bytes)
                mp3_bytes.seek(0)
            st.subheader("🔊 Nepali Speech")
            st.audio(
                mp3_bytes.read(),
                format="audio/mp3"
            )
    else:
        st.warning(
            "⚠️ No text could be detected from the uploaded image."
        )
        
# streamlit run task.py --server.address=0.0.0.0 --server.port=8502
