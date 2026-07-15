import streamlit as st
import joblib

model = joblib.load("news_model.joblib")
st.title("BBC News Classifier")
text = st.text_area("Enter News")

if st.button("Predict"):
    prediction = model.predict([text])[0]
    st.success(prediction)
    
# to run streamlit run streamlit_app.py