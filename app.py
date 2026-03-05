import streamlit as st
from agent import run_agent
from utils.pdf_generator import generate_resume_pdf

st.title("Resume Optimization Agent with ATS Improvement")

resume_file = st.file_uploader("Upload Resume (PDF)")
role = st.text_input("Enter Job Role (e.g., Data Scientist, ML Engineer)")

if st.button("Optimize Resume"):
    results = run_agent(resume_file, role)

    st.subheader("📊 ATS Score Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Initial ATS Score", f"{results['initial_score']}%")

    with col2:
        st.metric("Final ATS Score", f"{results['final_score']}%",
                  delta=results['final_score'] - results['initial_score'])

    st.write(f"🔁 Iterations Used: {results['iterations']}")
    st.subheader("Missing Skills (Before)")
    st.write(results["initial_missing"])
    st.subheader("Missing Skills (After)")
    st.write(results["final_missing"])
    st.subheader("📝 Optimized Resume")
    st.text_area("Final Resume", results["improved_resume"], height=400)
    pdf_path = generate_resume_pdf(results["improved_resume"])

    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📄 Download Optimized Resume (PDF)",
            data=f,
            file_name="optimized_resume.pdf",
            mime="application/pdf"
        )