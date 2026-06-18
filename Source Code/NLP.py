import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# nltk.download("punkt")
# nltk.download("stopwords")
from langdetect import detect


try:
    choice = input("Enter 1 for user text or 2 for txt file: ")

    if choice == "1":
        org_text = input("Enter your text: ")

    elif choice == "2":
        path = input("Enter txt file path: ")

        try:
            with open(path, "r", encoding="utf-8") as file:
                org_text = file.read()
        except FileNotFoundError:
            print("❌ File not found. Please check path.")
            exit()

    else:
        print("❌ Invalid choice")
        exit()

    # ================= SAFE CHECK =================
    if not org_text.strip():
        print("❌ Empty text provided")
        exit()

    print("\nText:")
    print(org_text)

    lang = detect(org_text)
    print("\nDetected Language:", lang)

    if lang != "en":
        print("⚠️ Warning: This model is optimized for English text.")

    # Sentence Segmentation
    from nltk.tokenize import sent_tokenize

    sentences = sent_tokenize(org_text)

    if len(sentences) == 0:
        print("❌ No sentences found")
        exit()

    print("\nSentence Segmentation:")
    for sentence in sentences:
        print(sentence)

    # Lowercasing
    text = org_text.lower()
    print("\nText to lower case:")
    print(text)

    # Tokenization
    tokens = word_tokenize(text)
    print("\nTokens:")
    print(tokens)

    # Stop-word Removal
    stop_words = set(stopwords.words('english'))
    filter_words = [word for word in tokens if word.isalnum() and word not in stop_words]

    print("\nFiltered Words:")
    print(filter_words)

    # C:\Users\Hp\Desktop\sample.txt
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)
    words = vectorizer.get_feature_names_out()

    print("TF-IDF Matrix (partial view):")
    print(tfidf_matrix.toarray()[:2])  # only first 2 sentences

    print("Feature Names (Words):")
    print(words[:10])

    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        sentence_scores[sentence] = tfidf_matrix[i].sum()

    print("sentence scoring:")
    print(sentence_scores)

    for sentence, score in sentence_scores.items():
        print("\nScore:", round(score, 3))
        print(sentence)

    from collections import Counter
    from nltk.tokenize import word_tokenize

    # ================= WORD FREQUENCY =================
    word_freq = Counter(filter_words)

    print("\n========== WORD FREQUENCY ==========")
    for word, freq in word_freq.most_common(10):
        print(word, ":", freq)

    # ================= KEYWORDS =================
    top_keywords = [word for word, freq in word_freq.most_common(10)]

    print("\n========== KEYWORDS ==========")
    print(top_keywords)

    # ================= SUMMARY LENGTH INPUT =================
    try:
        num_sentences = int(input("\nHow many sentences do you want in summary? "))
        if num_sentences <= 0:
            print("❌ Number must be greater than 0")
            exit()
    except ValueError:
        print("❌ Invalid number input")
        exit()

    from heapq import nlargest

    # Extract top sentences
    summary_sentences = nlargest(
        num_sentences,
        sentence_scores,
        key=sentence_scores.get
    )

    summary = " ".join(summary_sentences)

    # ================= FINAL OUTPUT SYSTEM =================
    print("\n========== ORIGINAL TEXT ==========")
    print(org_text)

    print("\n========== GENERATED SUMMARY ==========")
    print(summary)

except Exception as e:
    print("❌ Unexpected error occurred:", str(e))