import streamlit as st
from agent import run_agent

st.title("Resume Optimization Agent with ATS Improvement")

resume_file = st.file_uploader("Upload Resume (PDF)")
jd_text = st.text_area("Paste Job Description")

if st.button("Optimize Resume"):
    results = run_agent(resume_file, jd_text)

    st.subheader("📊 ATS Score Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Initial ATS Score", f"{results['initial_score']}%")

    with col2:
        st.metric("Final ATS Score", f"{results['final_score']}%",
                  delta=results['final_score'] - results['initial_score'])

    st.write(f"🔁 Iterations Used: {results['iterations']}")

    st.subheader("❌ Missing Skills (Before Optimization)")
    if results["initial_missing"]:
        st.write(results["initial_missing"])
    else:
        st.success("No missing skills detected!")

    st.subheader("⚠ Remaining Missing Skills (After Optimization)")
    if results["final_missing"]:
        st.write(results["final_missing"])
    else:
        st.success("All key skills covered!")

    st.subheader("📝 Optimized Resume")
    st.text_area("Final Resume", results["improved_resume"], height=400)