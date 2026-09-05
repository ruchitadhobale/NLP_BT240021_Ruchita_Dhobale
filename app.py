import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.set_page_config(
    page_title="Student Feedback Analyzer",
    page_icon="😊"
)

st.title("😊 Student Feedback Sentiment Analyzer")
st.write("Analyze student feedback using NLP and Machine Learning.")

# Training data
texts = [
    "The teacher explains concepts very clearly",
    "Excellent teaching and very helpful teacher",
    "I really enjoyed the lectures",
    "The subject is interesting and easy to understand",
    "The teacher is supportive and good",
    "Very good teaching method",
    "The lectures are confusing",
    "Teaching is very poor",
    "I did not understand the concepts",
    "The lectures are too fast",
    "The teacher does not explain properly",
    "Very bad teaching experience"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative"
]

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# User input
feedback = st.text_area(
    "Enter Student Feedback:",
    placeholder="Example: The teacher explains everything very clearly..."
)

# Analyze button
if st.button("🔍 Analyze Sentiment"):

    if feedback.strip() == "":
        st.warning("⚠️ Please enter some feedback.")

    else:
        feedback_vector = vectorizer.transform([feedback])

        prediction = model.predict(feedback_vector)[0]

        if prediction == "Positive":
            st.success("😊 Sentiment: POSITIVE")
        else:
            st.error("😞 Sentiment: NEGATIVE")
