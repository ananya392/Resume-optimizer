from tools.parser import parse_resume
from tools.keyword_extractor import extract_keywords
from tools.matcher import calculate_ats_score
from tools.rewriter import rewrite_resume

MAX_ITERATIONS = 3

def run_agent(resume_file, jd_text):
    resume_text = parse_resume(resume_file)
    keywords = extract_keywords(jd_text)

    # Initial score
    initial_score, initial_missing = calculate_ats_score(resume_text, keywords)

    iteration = 0
    current_score = initial_score
    current_missing = initial_missing

    while current_score < 80 and iteration < MAX_ITERATIONS:
        resume_text = rewrite_resume(resume_text, current_missing)
        current_score, current_missing = calculate_ats_score(resume_text, keywords)
        iteration += 1

    final_score = current_score
    final_missing = current_missing

    return {
        "initial_score": initial_score,
        "final_score": final_score,
        "initial_missing": initial_missing,
        "final_missing": final_missing,
        "iterations": iteration,
        "improved_resume": resume_text
    }