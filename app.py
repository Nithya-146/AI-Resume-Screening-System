import streamlit as st
from resume_parser import extract_text
from skill_extractor import extract_skills
from similarity import calculate_similarity

st.title("AI Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:

    resume_text = extract_text(uploaded_file)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description.lower())

    score = calculate_similarity(resume_text, job_description)

    missing_skills = list(set(job_skills) - set(resume_skills))

    st.subheader("Match Score")
    st.write(score,"%")

    st.subheader("Resume Skills")
    st.write(resume_skills)

    st.subheader("Required Skills")
    st.write(job_skills)

    st.subheader("Missing Skills")
    st.write(missing_skills)