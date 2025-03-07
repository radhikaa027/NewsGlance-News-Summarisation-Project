# NewsGlance – News Summarization Project

Welcome to *NewsGlance, an AI-driven news summarization system that provides concise and coherent summaries of lengthy news articles. This project explores multiple approaches—both **extractive* and *abstractive*—to automatically summarize text using state-of-the-art Natural Language Processing (NLP) techniques.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)   
3. [Methodology](#methodology)  
   - [Extractive Summarization](#extractive-summarization)  
   - [Abstractive Summarization](#abstractive-summarization)  
4. [Dataset](#dataset)  
5. [Fine-Tuned Model](#fine-tuned-model)  
6. [Installation & Requirements](#installation--requirements)  
7. [How to Run](#how-to-run)  
8. [Usage](#usage)  
9. [Results](#results)  
10. [Future Work](#future-work)  
11. [References](#references)  
12. [License](#license)  
13. [Contact](#contact)  

---

## 1. Project Overview

*NewsGlance* is designed to help users quickly grasp the key information in lengthy news articles. It combines two major text summarization paradigms:

- *Extractive Summarization*: Selecting the most important sentences from the source text.
- *Abstractive Summarization*: Generating new sentences that capture the essence of the original text, much like a human-written summary.

We employ multiple techniques, ranging from simple frequency-based methods to advanced transformer-based models (T5). Our goal is to make news consumption more efficient and user-friendly by providing short, accurate, and coherent summaries.

---

## 2. Features

- *Multiple Summarization Methods*: 
  - *Extractive*: Frequency-based, TF-IDF-based.  
  - *Abstractive*: RNN with Attention, T5 Transformer.
- *Streamlit Web App*: Easy-to-use interface to input news articles and instantly view summaries.
- *Scalability*: Can be extended to handle larger datasets or integrated into other NLP pipelines.
- *Customizable*: Users can easily tweak parameters such as summary length, threshold scores, etc.
![image](https://github.com/user-attachments/assets/19eeccef-5ff9-4f56-afd9-e282ea804b7e)
---

## 3. Methodology

This project implements *four* main approaches to text summarization:

### Extractive Summarization

1. *Frequency-Based Approach*  
   - *Idea*: Rank each sentence by the sum of the normalized frequencies of words in it.  
   - *Pros*: Simple and interpretable.  
   - *Cons*: Might miss context; purely statistical.

2. *TF-IDF-Based Approach*  
   - *Idea*: Convert each sentence to a TF-IDF vector, score them, and pick the top k.  
   - *Pros*: Gives more weight to domain-specific or rare yet important words.  
   - *Cons*: Still bound by original text sentences; lacks paraphrasing.

### Abstractive Summarization

1. *RNN (Seq2Seq) with Attention*  
   - *Idea*: An encoder-decoder framework using GRU or LSTM. The encoder processes the text, and the decoder generates new summary sentences with an attention mechanism.  
   - *Pros*: Produces more human-like summaries than extractive methods.  
   - *Cons*: Can struggle with very long inputs; might generate repetitive or off-topic text.

2. *T5 Transformer*  
   - *Idea*: Fine-tune Google’s T5 (Text-to-Text Transfer Transformer) model on the CNN/DailyMail dataset.  
   - *Pros*: State-of-the-art performance, powerful pretraining, handles longer context well.  
   - *Cons*: Computationally heavier than RNNs, requires GPU for efficient training.

---

## 4. Dataset

We use the *CNN/DailyMail* dataset, a widely recognized benchmark for news summarization tasks. It contains over 300,000 articles along with human-written “highlights.”

- *Source*: [CNN/DailyMail on HuggingFace](https://huggingface.co/datasets/abisee/cnn_dailymail)  
- *Structure*:  
  - *article*: Full text of the news article.  
  - *highlights*: Human-written summary (reference).  
- *Splits*: Train / Validation / Test.

You can download the dataset from the link above or directly load it via Hugging Face datasets library:

python
from datasets import load_dataset

dataset = load_dataset("abisee/cnn_dailymail", "3.0.0")


---

## 5. Fine-Tuned Model

We have fine-tuned a *T5-small* model on the CNN/DailyMail dataset to improve the abstractive summarization performance. You can find and download our fine-tuned model here:

- *Hugging Face Model Hub*:  
  [Deepanshu7284/t5-small-finetuned-cnn-news](https://huggingface.co/Deepanshu7284/t5-small-finetuned-cnn-news)

Using it is straightforward with the Hugging Face transformers library:

python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("Deepanshu7284/t5-small-finetuned-cnn-news")
model = T5ForConditionalGeneration.from_pretrained("Deepanshu7284/t5-small-finetuned-cnn-news")


---

## 6. Installation & Requirements

1. *Clone this repository*:
   bash
   git clone https://github.com/deepanshu-agg/NewsGlance_News-Summarisation-Project.git
   cd NewsGlance_News-Summarisation-Project
   

2. *Install Dependencies*:  
   Make sure you have Python 3.7+ installed. Then install required packages:
   bash
   pip install -r requirements.txt
   
   *If requirements.txt is missing or incomplete, you may need the following major libraries:*
   - streamlit
   - transformers
   - torch
   - datasets
   - nltk
   - scikit-learn
   - numpy
   - pandas

3. *(Optional) GPU Setup*:  
   If you plan to train or fine-tune the models, having a GPU (NVIDIA CUDA) is recommended.

---

## 7. How to Run

To launch the *Streamlit* application, navigate to the StreamlitApp folder (or the project root, depending on your setup) and run:

bash
streamlit run highlights_app.py


- This command starts a local web server.
- A browser window will open automatically (or you can manually open the URL shown in the terminal, typically http://localhost:8501).

---

## 8. Usage

1. *Open the Web App*  
   After running the streamlit run highlights_app.py command, your browser should display the NewsGlance interface.

2. *Paste or Enter News Article*  
   - You can paste any news article text into the provided text box.

3. *Select Summarization Method*  
   - *Extractive (TF-IDF)* or *Abstractive (T5)*.  
   - (Some versions of the app may also allow you to select Frequency-based or RNN-based from a dropdown.)

4. *View Summary*  
   - The app will display the summarized text in a matter of seconds.

5. *Compare*  
   - Optionally, you can compare different summaries by toggling between approaches.

---

## 9. Results

We evaluated our approaches using standard metrics such as *ROUGE, **METEOR, and **BERTScore*:

- *Extractive (TF-IDF)* consistently outperformed a simple Frequency-based method in ROUGE scores and overall coherence.
- *Abstractive (T5)* significantly outperformed RNN-based abstractive methods in capturing context and producing fluent summaries.

You can refer to the PDF report (Group_No11_NewsGlance_News_Summarisation_Report.pdf) for a detailed breakdown of experiments and evaluation metrics.

---

## 10. Future Work

1. *Hybrid Approach*: Combine extractive pre-selection of sentences with abstractive rewriting for improved factual accuracy and fluency.  
2. *Domain-Specific Summarization*: Fine-tune on specialized corpora (finance, medical, legal) to enhance domain-specific summarization quality.  
3. *Multi-Lingual Support*: Extend the pipeline to handle non-English news articles.  
4. *Advanced Evaluation*: Incorporate new metrics that measure factual correctness and coherence more effectively than standard ROUGE.  
5. *Explainable AI*: Provide insights into why certain sentences or phrases are selected/generated to increase transparency.

---

## 11. References

- *Dataset*: [CNN/DailyMail on HuggingFace](https://huggingface.co/datasets/abisee/cnn_dailymail)  
- *Fine-Tuned Model*: [Deepanshu7284/t5-small-finetuned-cnn-news](https://huggingface.co/Deepanshu7284/t5-small-finetuned-cnn-news)  
- *Key Papers & Libraries*:  
  - [Hugging Face Transformers](https://github.com/huggingface/transformers)  
  - [PyTorch](https://pytorch.org/) or [TensorFlow](https://www.tensorflow.org/)  
  - [ROUGE Metric](https://github.com/pltrdy/rouge)  

For a complete literature survey and methodology, please see the accompanying project report PDF in this repository.

---

## 12. License

This project is open-source. If you plan to use or modify the code, please check the license details (if provided in this repo). Contributions and forks are welcome!

---

## 13. Contact

If you have any questions, suggestions, or issues running the code, feel free to reach out:

- *Author*: [Deepanshu Aggarwal](https://github.com/radhikaa027)
- *Email*: [radhikabhati218@gmail.com](mailto:radhikabhati218@gmail.com)

We hope *NewsGlance* helps you quickly stay informed with concise and accurate news summaries. Happy summarizing!
