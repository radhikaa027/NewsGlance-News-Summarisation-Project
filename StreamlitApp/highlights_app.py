import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image
from transformers import pipeline
from summarize import NewsSummarization

# Load model
hub_model_id = "Deepanshu7284/t5-small-finetuned-cnn-news"
summarizer = pipeline("summarization", model=hub_model_id)

# Create header
st.write("""# WELCOME TO NEWSGLANCE! \n ### A News Summarizer""")
st.write("Provide a news article and get a summary within seconds!")

# Display image
image = Image.open('newsglance.jpg')
st.image(image)

# Create and name sidebar
st.sidebar.header('Select summary parameters')
with st.sidebar.form("input_form"):
    st.write('Select summary length for extractive summary')
    max_sentences = st.slider('Summary Length', 1, 10, step=1, value=3)
    st.write('Select word limits for abstractive summary')
    max_words = st.slider('Max words', 50, 200, step=10, value=200)
    min_words = st.slider('Min words', 10, 100, step=10, value=100)
    submit_button = st.form_submit_button("Summarize!")

# Input text area
article = st.text_area(label="Enter the article you want to summarize", height=300, value="Enter Article Body Here")

# Initialize News Summarization class
news_summarizer = NewsSummarization()

# Session states to store summaries
if 'extractive_summary' not in st.session_state:
    st.session_state.extractive_summary = ""
if 'abstractive_summary' not in st.session_state:
    st.session_state.abstractive_summary = ""

# Generate summaries on button click
if submit_button:
    st.session_state.extractive_summary = news_summarizer.extractive_summary(article, num_sentences=max_sentences)
    st.session_state.abstractive_summary = summarizer(article, max_length=max_words, min_length=min_words, do_sample=False)[0]['summary_text']

    st.write("## Extractive Summary")
    st.write(st.session_state.extractive_summary)

    st.write("## Abstractive Summary")
    st.write(st.session_state.abstractive_summary)

# Sidebar explanation about summarization
with st.sidebar.expander("More About Summarization"):
    st.markdown("""
        In extractive summarization, we identify important sentences from the article and make a summary by selecting the most important sentences.<br>

        For abstractive summarization, the model understands the context and generates a summary with the important points using new phrases and language. 
        Abstractive summarization is more similar to the way a human summarizes content. A person might read the entire document, 
        remember a few key points, and while writing the summary, will create new sentences that include these points. Abstractive summarization follows the same concept.
    """)
