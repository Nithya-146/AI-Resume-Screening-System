import re
from skills_db import skills

def extract_skills(text):
    # remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    found = []
    for skill in skills:
        if skill.lower() in text:
            found.append(skill)
    return found