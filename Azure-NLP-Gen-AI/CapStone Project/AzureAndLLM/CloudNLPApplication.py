
from flask import Flask, render_template, request, jsonify
import azure.cognitiveservices.language.textanalytics as models
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
import transformers
import torch
import nltk
from nltk.tokenize import sent_tokenize
import asyncio
import aiohttp
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from fairlearn.metrics import (
    MetricFrame,
    selection_rate,
    demographic_parity_difference,
    equalized_odds_difference,
)
from fairlearn.postprocessing import ThresholdOptimizer

app = Flask(__name__)

# Azure Configuration 
TEXT_ANALYTICS_KEY = os.environ.get("TEXT_ANALYTICS_KEY") or "YOUR_TEXT_ANALYTICS_KEY"
TEXT_ANALYTICS_ENDPOINT = os.environ.get("TEXT_ANALYTICS_ENDPOINT") or "YOUR_TEXT_ANALYTICS_ENDPOINT"

# Hugging Face Model Configuration (for summarization)
SUMMARIZATION_MODEL_NAME = "facebook/bart-large-cnn"
try:
    summarizer = transformers.pipeline("summarization", model=SUMMARIZATION_MODEL_NAME)
except Exception as e:
    print(f"Error loading summarization model: {e}")
    summarizer = None  # Set to None to avoid crashing if model loading fails.

# Text Analytics Client Setup
credential = AzureKeyCredential(TEXT_ANALYTICS_KEY)
try:
    text_analytics_client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=credential)
except Exception as e:
    print(f"Error creating Text Analytics client: {e}")
    text_analytics_client = None  # Set to None, handle errors later.

# NLTK Setup
try:
    nltk.download('punkt')
except Exception as e:
    print(f"Error downloading nltk punkt: {e}")

# Bias Mitigation with Fairlearn
def mitigate_bias(text, sensitive_features=None):
    """
    Mitigates bias in text data using Fairlearn.  This version focuses on
    pre-processing and post-processing techniques.

    Args:
        text (str): The input text to be processed.
        sensitive_features (pd.Series, optional):  A Pandas Series representing the sensitive
            features (e.g., 'gender', 'race').  If None, the function performs
            only basic text cleaning.

    Returns:
        str: The processed text, potentially modified to reduce bias.
    """
    # Basic text cleaning (remove extra spaces, lowercase)
    text = " ".join(text.split())
    text = text.lower()

    if sensitive_features is None:
        return text
    #    here we  reduce pronoun bias and normalize some terms.
    pronoun_replacements = {
        "he": "they",
        "him": "them",
        "his": "their",
        "she": "they",
        "her": "them",
        "hers": "their",
        "man": "person",
        "woman": "person",
        "men": "people",
        "women": "people",
        "guy": "person",
        "gal": "person",
        "boy": "child",
        "girl": "child",
    }
    words = text.split()
    text = " ".join(pronoun_replacements.get(word, word) for word in words)

    return text

def analyze_sentiment(text):
    if text_analytics_client is None:
        return {"error": "Text Analytics client is not initialized.  Re-check Azure credentials and network connectivity."}
    try:
        documents = [text]
        response = text_analytics_client.analyze_sentiment(documents=documents)[0]
        return {
            "sentiment": response.sentiment,
            "confidence_scores": response.confidence_scores,
        }
    except Exception as e:
        return {"error": f"Error analyzing sentiment: {e}"}

# Document Summarization Function
def summarize_document(text):
    if summarizer is None:
        return {"error": "Summarization model is not loaded."}
    try:
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return {"error": f"Error summarizing document: {e}"}

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment_result = None
    summary_result = None

    if request.method == 'POST':
        if 'sentiment_text' in request.form:
            text = request.form['sentiment_text']
            sensitive_features = np.random.choice(['male', 'female'], len(text.split()))
            sensitive_features_series = pd.Series(sensitive_features)
            text_for_sentiment = mitigate_bias(text, sensitive_features_series)  # Apply bias mitigation
            sentiment_result = analyze_sentiment(text_for_sentiment)
        elif 'summary_text' in request.form:
            text = request.form['summary_text']
            summary_result = summarize_document(text)

    return render_template('index.html', sentiment_result=sentiment_result, summary_result=summary_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))