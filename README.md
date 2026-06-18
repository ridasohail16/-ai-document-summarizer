# 📄 AI-Powered Document Summarization System

> **Teyzix Core Internship – June Batch | Task ID: AI-INT-1**
> Domain: Artificial Intelligence / NLP | 

---

## 📌 Overview

An AI-based system that automatically summarizes long text documents into short, meaningful summaries while preserving key information. Built using Python and NLP techniques to solve the real-world problem of manual, time-consuming document review.

This project includes **two modes**:
- 🐍 **Python Script** — Command-line based summarization using NLTK
- 🌐 **Streamlit Web UI** — Interactive live summarization in the browser

---

## 🚀 Features

- 📥 **Two Input Modes** — Accept text from `.txt` files or direct user input
- 🔤 **Text Preprocessing** — Lowercasing, stopword removal, tokenization, sentence segmentation
- 🧠 **Extractive Summarization** — TF-IDF based scoring + frequency-based sentence ranking
- 🔑 **Keyword Extraction** — Automatically extracts the most important keywords
- 📊 **Sentence Scoring** — Ranks sentences by importance using NLP techniques
- 📈 **Word Frequency Analysis** — Breakdown of most used words
- 📤 **Export Output** — Save summaries as `.txt`
- 🌐 **Live Streamlit UI** — Summarize documents in real-time through a web interface
- ⚙️ **Adjustable Summary Length** — Control how long or short the summary is

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| NLTK | Tokenization, stopword removal, sentence segmentation |
| collections | Word frequency analysis |
| scikit-learn | TF-IDF vectorization |
| Streamlit | Interactive web UI for live summarization |

---

## 📁 Project Structure

```
ai-document-summarizer/
│
├── Source Code/
│   ├── python/              # Core NLP summarization script
│   │   └── summarizer.py    # TF-IDF, keyword extraction, sentence scoring
│   │
│   └── StreamLit UI/        # Web-based live summarization
│       └── app.py           # Streamlit application
│
├── Sample Document/         # Input .txt documents used for testing
├── Generated Summaries/     # Output summaries produced by the system
├── Execution Screenshots/
│   ├── python/              # Screenshots of Python script running
│   └── StreamLit UI/        # Screenshots of Streamlit web app
│
└── Readme/
    └── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ridasohail16/ai-document-summarizer.git
cd ai-document-summarizer
```

### 2. Install Dependencies
```bash
pip install nltk scikit-learn streamlit
```

### 3. Download NLTK Data
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

---

## 💻 How to Run

### 🐍 Python Script (Command Line)
```bash
cd "Source Code/python"
python summarizer.py
```

**What it does:**
- Takes input as direct text or loads a `.txt` file
- Preprocesses text (lowercase, stopwords, tokenization)
- Scores sentences using TF-IDF and word frequency
- Extracts top keywords using `collections`
- Displays summary + keyword list + sentence scores
- Exports summary as `.txt` file

---

### 🌐 Streamlit Web UI (Live Summarization)
```bash
cd "Source Code/StreamLit UI"
streamlit run app.py
```

Then open your browser and go to:
```
http://localhost:8501
```

**What it does:**
- Opens a clean web interface in your browser
- Paste text directly or upload a `.txt` file
- Adjust summary length with a slider
- See the summary generated instantly in real-time
- View top keywords and word frequency
- Download the summary with one click

---

## 📊 Evaluation Criteria Met

| Criteria | Weight | Status |
|---------|--------|--------|
| NLP Preprocessing | 25% | ✅ |
| Summarization Logic | 25% | ✅ |
| Code Structure | 20% | ✅ |
| Output Quality | 15% | ✅ |
| Error Handling | 10% | ✅ |
| Documentation | 5% | ✅ |

---

## 🏆 Bonus Features Implemented

- ✅ **Streamlit UI** — Live summarization through interactive web interface
- ✅ **TF-IDF Scoring** — Advanced sentence ranking
- ✅ **Keyword Extraction** — Key terms highlighted from document

---

## 👩‍💻 Author

**Rida Sohail**
Teyzix Core Internship — June Batch 2026
Task ID: AI-INT-1
GitHub: [@ridasohail16](https://github.com/ridasohail16)

---

## 📃 License

This project was developed as part of the Teyzix Core Internship program.
