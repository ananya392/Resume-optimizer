import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords_local(jd_text):
    doc = nlp(jd_text)

    keywords = set()

    for token in doc:
        # Capture nouns and proper nouns
        if token.pos_ in ["NOUN", "PROPN"]:
            if not token.is_stop and token.is_alpha:
                keywords.add(token.text.lower())

    # Capture noun chunks (important for skills like "machine learning")
    for chunk in doc.noun_chunks:
        keywords.add(chunk.text.lower())

    return list(keywords)