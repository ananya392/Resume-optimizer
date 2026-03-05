import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Common words we don't want as skills
GENERIC_TERMS = {
    "system","work","ability","knowledge","experience","data",
    "team","project","analysis","task","role","process",
    "business","organization","problem","solution"
}

def extract_keywords_local(text):

    doc = nlp(text)

    keywords = set()

    # 1️⃣ Extract noun phrases (best for skills like "machine learning")
    for chunk in doc.noun_chunks:
        phrase = chunk.text.lower().strip()

        if len(phrase) > 2:
            keywords.add(phrase)

    # 2️⃣ Extract important nouns / proper nouns
    for token in doc:

        if token.pos_ in ["NOUN","PROPN"]:

            word = token.text.lower()

            if (
                not token.is_stop
                and token.is_alpha
                and word not in GENERIC_TERMS
                and len(word) > 2
            ):
                keywords.add(word)

    # 3️⃣ Normalize keywords
    cleaned_keywords = []

    for k in keywords:

        k = re.sub(r"[^a-zA-Z0-9\s]", "", k).strip()

        if len(k) > 2:
            cleaned_keywords.append(k)

    return sorted(list(set(cleaned_keywords)))