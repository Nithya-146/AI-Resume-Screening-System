from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume, job_desc):

    documents = [resume, job_desc]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    return round(similarity[0][0] * 100, 2)