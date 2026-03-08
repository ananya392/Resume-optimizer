import re

SECTION_WEIGHTS = {
    "skills": 0.4,
    "technical skills": 0.4,
    "experience": 0.3,
    "work experience": 0.3,
    "projects": 0.2,
    "personal projects": 0.2,
    "other": 0.1
}


def split_sections(resume_text):

    sections = {}
    current_section = "other"

    for line in resume_text.split("\n"):

        line_clean = line.strip().lower()

        if line_clean in SECTION_WEIGHTS:
            current_section = line_clean
            sections[current_section] = []
            continue

        sections.setdefault(current_section, []).append(line)

    return sections


def calculate_ats_score(resume_text, keywords):

    resume_text = resume_text.lower()

    sections = split_sections(resume_text)

    total_score = 0
    matched_keywords = set()
    missing_keywords = []

    for keyword in keywords:

        keyword = keyword.lower()
        found = False

        for section, content in sections.items():

            section_text = " ".join(content)

            if re.search(rf"\b{re.escape(keyword)}\b", section_text):

                weight = SECTION_WEIGHTS.get(section, SECTION_WEIGHTS["other"])
                total_score += weight * 100 / len(keywords)

                matched_keywords.add(keyword)
                found = True
                break

        if not found:
            missing_keywords.append(keyword)

    final_score = min(total_score, 100)

    return round(final_score, 2), missing_keywords