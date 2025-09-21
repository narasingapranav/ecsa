import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re, string
import nltk
from transformers import pipeline

# --------------------------
# Setup
# --------------------------
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# --------------------------
# Helper Functions
# --------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r'\d+', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# Split text into chunks for summarization
def chunk_text(text, max_chunk_size=800):
    words = text.split()
    return [" ".join(words[i:i + max_chunk_size]) for i in range(0, len(words), max_chunk_size)]

# --------------------------
# Load Models
# --------------------------
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

# --------------------------
# Streamlit App
# --------------------------
st.title("MCA e-Consultation Sentiment Analysis")
st.write("Analyze stakeholder comments, view sentiment, summaries, and word clouds.")

# --------------------------
# Upload Dataset
# --------------------------
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # --------------------------
    # Preprocessing
    # --------------------------
    df["cleaned"] = df["comment_text"].apply(clean_text)

    # --------------------------
    # Sentiment Analysis
    # --------------------------
    st.subheader("Sentiment Analysis")
    df["predicted_sentiment"] = df["cleaned"].apply(lambda x: sentiment_model(x[:512])[0]['label'])
    st.dataframe(df[["comment_text", "predicted_sentiment"]].head(10))

    # --------------------------
    # Word Cloud
    # --------------------------
    st.subheader("Word Cloud")
    all_text = " ".join(df["cleaned"].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

    # --------------------------
    # Sentiment Distribution
    # --------------------------
    st.subheader("Sentiment Distribution")
    st.bar_chart(df["predicted_sentiment"].value_counts())

    # --------------------------
    # Summarization
    # --------------------------
    st.subheader("Summary of All Comments")

    if len(all_text.split()) > 0:
        # Split into chunks if too large
        text_chunks = chunk_text(all_text)
        summaries = []

        for i, chunk in enumerate(text_chunks):
            st.write(f"Processing chunk {i + 1} of {len(text_chunks)}...")
            result = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
            summaries.append(result[0]['summary_text'])

        # Combine summaries into one final summary
        final_summary_text = " ".join(summaries)

        # Summarize the combined summary for a concise output
        final_output = summarizer(final_summary_text, max_length=120, min_length=50, do_sample=False)
        summary_text = final_output[0]['summary_text']

        st.write("### Final Summary")
        st.success(summary_text)
    else:
        st.warning("No comments found to summarize.")

    # --------------------------
    # Download Results
    # --------------------------
    df.to_csv("results_with_sentiment.csv", index=False)
    st.download_button(
        label="Download Results CSV",
        data=df.to_csv(index=False),
        file_name="results_with_sentiment.csv",
        mime="text/csv"
    )
