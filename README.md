# NLP Applied Project – Student Feedback Sentiment Analyzer

## Student Details

**Name:** Ruchita Dnyaneshwar Dhobale  
**Roll No.:** BT240021ET  
**Course:** Natural Language Processing (ET5M004)  
**Semester/Branch:** V Semester ETC

## 1. Problem Statement

Manual analysis of a large number of student feedback responses is time-consuming. It is difficult to identify the overall opinion of students manually.

This project develops an NLP-based application that automatically analyzes student feedback and classifies it as Positive or Negative.

## 2. Objective

- To analyze student feedback automatically.
- To apply Natural Language Processing techniques.
- To classify feedback into Positive and Negative categories.
- To develop a simple and interactive web application.
- To demonstrate a real-world application of NLP.

## 3. Introduction

Student feedback provides valuable information about teaching quality and students' opinions.

Sentiment Analysis is an NLP technique used to identify the sentiment expressed in text.

This project uses TF-IDF to convert feedback text into numerical features and a Machine Learning model to predict the sentiment.

## 4. NLP Technique / Method Used

### TF-IDF

TF-IDF stands for Term Frequency-Inverse Document Frequency.

It converts text into numerical features that can be used by a Machine Learning model.

### Sentiment Classification

The system classifies student feedback into:

- Positive
- Negative

## 5. Dataset / Source of Data

The project uses student feedback examples containing Positive and Negative sentiments.

Example:

| Feedback | Sentiment |
|---|---|
| The teacher explains concepts clearly. | Positive |
| The lectures are very interesting. | Positive |
| The teacher does not explain properly. | Negative |
| The lectures are confusing. | Negative |

## 6. Software / Tools / Libraries Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- TF-IDF Vectorizer
- Machine Learning

## 7. Methodology / Workflow

1. Collect student feedback.
2. Preprocess the text.
3. Convert text into numerical features using TF-IDF.
4. Train the Machine Learning model.
5. Accept feedback from the user.
6. Convert the new feedback into TF-IDF features.
7. Predict the sentiment.
8. Display the result.

## 8. Project Workflow

```text
Student Feedback
       ↓
Text Preprocessing
       ↓
TF-IDF Vectorization
       ↓
Machine Learning Model
       ↓
Sentiment Prediction
       ↓
Positive / Negative
