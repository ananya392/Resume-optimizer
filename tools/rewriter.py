import os
import google.generativeai as genai

# Configure API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY environment variable is not set. "
        "Set it before running the app (e.g. `export GEMINI_API_KEY=...`)."
    )
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def rewrite_resume(resume_text, missing_keywords):
    missing_str = ", ".join(missing_keywords)

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