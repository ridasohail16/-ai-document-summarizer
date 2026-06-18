import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from heapq import nlargest
from langdetect import detect

# OPTIONAL transformer
try:
    from transformers import pipeline
    transformer_available = True
except:
    transformer_available = False

nltk.download("punkt")
nltk.download("stopwords")


# ================= UI =================
st.set_page_config(page_title="NLP Summarizer", layout="wide")

st.title("🧠 AI Text Summarizer")
st.write("Upload text or paste content to generate extractive & AI summaries")

text = st.text_area("Enter your text here:")

num_sentences = st.slider("Summary length (sentences)", 1, 5, 2)


# ================= PROCESS =================
if st.button("Generate Summary"):

    if not text.strip():
        st.error("Please enter text")
    else:

        # Language detection
        lang = detect(text)
        st.info(f"🌍 Detected Language: {lang}")

        # Sentence tokenization
        sentences = sent_tokenize(text)

        if len(sentences) == 0:
            st.error("No sentences found")
        else:

            # Lowercase + tokens
            tokens = word_tokenize(text.lower())

            stop_words = set(nltk.corpus.stopwords.words('english'))
            filter_words = [w for w in tokens if w.isalnum() and w not in stop_words]

            # TF-IDF
            vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(sentences)

            words = vectorizer.get_feature_names_out()

            sentence_scores = {}

            for i, sentence in enumerate(sentences):
                score = tfidf_matrix[i].sum()
                sentence_scores[sentence] = score / (len(sentence.split()) + 1)

            # Word frequency
            word_freq = Counter(filter_words)

            # ================= OUTPUT =================

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📌 Original Text")
                st.write(text)

                st.subheader("🔑 Top Keywords")
                st.write([w for w, f in word_freq.most_common(10)])

            with col2:
                st.subheader("📊 Sentence Scores")
                st.write(sentence_scores)

            # SUMMARY
            summary_sentences = nlargest(
                num_sentences,
                sentence_scores,
                key=sentence_scores.get
            )

            summary = " ".join(summary_sentences)

            st.subheader("📝 Extractive Summary")
            st.success(summary)

            # ================= TRANSFORMER =================
            if transformer_available:

                if st.button("Generate AI (Abstractive) Summary"):

                    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

                    short_text = text[:2000]

                    result = summarizer(short_text, max_length=120, min_length=40, do_sample=False)

                    st.subheader("🤖 AI Summary (Transformer)")
                    st.info(result[0]['summary_text'])