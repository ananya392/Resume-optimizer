import re

def extract_keyword_list(keywords):
    # Handle both list and string inputs
    if isinstance(keywords, list):
        return [k.strip().lower() for k in keywords if k.strip()]
    # If string, split by comma or newline
    keyword_list = re.split(r',|\n', keywords)
    return [k.strip().lower() for k in keyword_list if k.strip()]

def calculate_ats_score(resume_text, keywords):
    resume_lower = resume_text.lower()
    keywords_list = extract_keyword_list(keywords)

    matched_keywords = []
    for word in keywords_list:
        if word in resume_lower:
            matched_keywords.append(word)

    score = (len(matched_keywords) / len(keywords_list)) * 100 if keywords_list else 0

    missing = list(set(keywords_list) - set(matched_keywords))

    return round(score, 2), missing