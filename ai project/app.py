import streamlit as st
import joblib
import re
import string

# Load trained models
model = joblib.load("mental_health_sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
scaler = joblib.load("scaler.pkl")

# Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    return text

# Streamlit UI
st.title("Mental Health Sentiment Analyzer")
st.write("Type a sentence and the model will predict its sentiment.")

user_input = st.text_area("Enter text here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        cleaned = clean_text(user_input)
        vect = vectorizer.transform([cleaned])
        vect = scaler.transform(vect)
        prediction = model.predict(vect)[0]
        st.success(f"Predicted Sentiment: **{prediction}**")
