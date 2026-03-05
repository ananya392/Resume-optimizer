import re

def calculate_ats_score(resume_text, keywords):

    resume = resume_text.lower()

    total_keywords = len(keywords)

    matched_keywords = []
    missing_keywords = []

    frequency_count = 0

    for skill in keywords:

        skill = skill.lower()

        occurrences = len(re.findall(rf"\b{re.escape(skill)}\b", resume))

        if occurrences > 0:
            matched_keywords.append(skill)
            frequency_count += occurrences
        else:
            missing_keywords.append(skill)

    # 1️⃣ Keyword coverage score
    keyword_score = (len(matched_keywords) / total_keywords) * 100 if total_keywords else 0

    # 2️⃣ Frequency score
    frequency_score = min((frequency_count / (total_keywords * 2)) * 100, 100)

    # 3️⃣ Skill diversity score
    unique_skills = len(set(matched_keywords))
    diversity_score = (unique_skills / total_keywords) * 100 if total_keywords else 0

    # Weighted final score
    final_score = (
        0.5 * keyword_score +
        0.3 * frequency_score +
        0.2 * diversity_score
    )

    return round(final_score,2), missing_keywords