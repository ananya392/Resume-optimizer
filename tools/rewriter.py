import google.generativeai as genai

# Configure API key
genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

def rewrite_resume(resume_text, missing_skills):
    missing_str = ", ".join(missing_skills)

    prompt = f"""
    Improve the resume below to increase ATS score.

    Requirements:
    - Naturally include these missing skills: {missing_str}
    - Do NOT keyword stuff.
    - Strengthen bullet points with action verbs.
    - Keep it professional and concise.
    - Maintain realistic experience.

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text