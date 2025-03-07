# summarize.py

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re

# Ensure necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')

class NewsSummarization:
    def __init__(self):
        pass

    def clean_text(self, text):
        """
        Clean text by removing special characters, multiple spaces, and converting to lowercase.
        :param text: str, input text to clean
        :return: str, cleaned text
        """
        text = text.lower()
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        text = re.sub(r'[^a-zA-Z0-9. ]', '', text)  # Remove special characters
        return text

    def preprocess_and_tokenize(self, text):
        """
        Preprocess the text and tokenize it into sentences.
        :param text: str, input text to preprocess
        :return: list, tokenized sentences
        """
        cleaned_text = self.clean_text(text)
        sentences = sent_tokenize(cleaned_text)
        return sentences

    def extractive_summary(self, text, num_sentences=3):
        """
        Extractive summarization using TF-IDF to score sentences.
        :param text: str, input text to summarize
        :param num_sentences: int, number of sentences to include in the summary
        :return: str, extractive summary
        """
        # Tokenize text into sentences
        sentences = self.preprocess_and_tokenize(text)

        # If there are no sentences, return an empty summary
        if not sentences:
            return ""

        # Initialize TF-IDF Vectorizer
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(sentences)

        # Compute sentence scores as the sum of TF-IDF weights
        sentence_scores = tfidf_matrix.sum(axis=1).A.flatten()

        # Rank sentences by their scores and extract the top N
        ranked_sentences = sorted(
            ((score, idx) for idx, score in enumerate(sentence_scores)),
            reverse=True
        )

        # Select the top N sentences
        top_sentence_indices = [idx for _, idx in ranked_sentences[:num_sentences]]

        # Return the top sentences in the order they appear in the text
        summary = ' '.join([sentences[idx] for idx in sorted(top_sentence_indices)])
        return summary

