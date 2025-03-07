# NewsGlance – Automated News Summarisation

A comprehensive project that explores **extractive** and **abstractive** text summarization approaches on large news datasets. The goal is to deliver concise, coherent summaries for lengthy news articles—helping readers quickly grasp the key information.

---

## Table of Contents
1. [Overview](#overview)
2. [Project Features](#project-features)
3. [Approaches & Methodologies](#approaches--methodologies)
   - [Extractive Summaries](#1-extractive-summaries)
   - [Abstractive Summaries](#2-abstractive-summaries)
4. [Repository Structure](#repository-structure)
5. [Installation & Setup](#installation--setup)
6. [Usage](#usage)
7. [Evaluation Metrics](#evaluation-metrics)
8. [Streamlit Deployment](#streamlit-deployment)
9. [Results & Observations](#results--observations)
10. [Future Enhancements](#future-enhancements)
11. [Contributors](#contributors)
12. [License](#license)

---

## Overview
**NewsGlance** is an AI-driven summarization tool designed to automatically produce concise summaries of news articles.  
- **Dataset:** [CNN/DailyMail](https://paperswithcode.com/dataset/cnn-dailymail) – Over 300k news articles with human-written highlights.
- **Core Objective:** Provide ~100-word summaries for each article using both **extractive** and **abstractive** methods.

---

## Project Features
- **Multiple Summarization Approaches:**  
  - **Extractive:** Frequency-based and TF-IDF methods.
  - **Abstractive:** RNN with Attention and T5 Transformer models.
- **Jupyter Notebooks:** Demonstrations for data exploration, model training, and evaluation.
- **Streamlit App:** A user-friendly interface for generating summaries.
- **Evaluation:** Summaries evaluated using ROUGE, METEOR, and BERTScore metrics.

---

## Approaches & Methodologies

### 1. Extractive Summaries
- **Frequency-Based Approach:**  
  Ranks sentences based on word frequency to select the most important sentences.
- **TF-IDF Approach:**  
  Uses TF-IDF vectors to score and select sentences with high information density.

### 2. Abstractive Summaries
- **RNN with Attention:**  
  An encoder-decoder model that generates summaries by focusing on relevant parts of the text.
- **T5 Transformer:**  
  A state-of-the-art model that generates coherent, human-like summaries after fine-tuning on news data.

---

## Repository Structure
├── AI_project_final_word_file.docx
├── Extractive_One_Approach.ipynb           # Frequency-based approach
├── Extractive_Two_Approach.ipynb           # TF-IDF-based approach
├── Flow chart State space search.png
├── Group_No11_NewsGlance_News_Summarisation_Code
│   ├── ...
│   └── (Supporting scripts & code)
├── Group_No11_NewsGlance_News_Summarisation_PPT.pdf
├── Group_No11_NewsGlance_News_Summarisation_Plagiarism_Report.pdf
├── Group_No11_NewsGlance_News_Summarisation_Report.pdf
├── LLM_Approach.ipynb                      # Abstractive approach (T5 or other large model)
├── RNN_Approach.ipynb                      # Abstractive approach (RNN + Attention)
├── StreamlitApp/                           # Streamlit UI code
│   ├── highlights_app.py                   # Example Streamlit script
│   ├── newsglance.jpg
│   └── summarize.py
├── cnn-data/                               # CSV or data files
│   ├── train.csv
│   ├── test.csv
│   └── validation.csv
└── README.md                               # Project documentation (this file)

## Evaluation Metrics
Summaries are evaluated using:

**ROUGE:** (ROUGE-1, ROUGE-2, ROUGE-L) – Measures overlap of n-grams.
**METEOR:** Assesses semantic similarity through exact and stem matches.
**BERTScore:** Uses embeddings to evaluate semantic similarity.

## Features:
- Input or paste article text.
- View side-by-side Extractive (TF-IDF) and Abstractive (T5) summaries.
- Instant results for quick evaluation.
  
## Results & Observations
- Extractive (TF-IDF):
Provides high accuracy in capturing important sentences, though sometimes with redundancy.
- Abstractive (T5):
Produces fluent, coherent summaries with better overall readability.


License
This project is for academic and research purposes. Please refer to the LICENSE file for more details.

Thank you for checking out NewsGlance – we hope it helps you stay informed quickly and efficiently!
