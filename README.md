# Advanced AI Resume Screening System

An AI-powered system to analyze resumes against job descriptions using NLP and Machine Learning. 

## Features
- Resume parsing (PDF / DOCX)
- Skill extraction and missing skills detection
- Match score calculation (TF-IDF + Cosine Similarity)
- Interactive dashboard with Streamlit
- Multi-resume ranking
- Export results to CSV

## Technologies Used
- Python
- Streamlit
- NLP (TF-IDF, Cosine Similarity)
- PyPDF2, python-docx
- Pandas, Scikit-learn

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
