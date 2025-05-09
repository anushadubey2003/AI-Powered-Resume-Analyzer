import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def parse_resume(file_path):
    text = extract_text(file_path)
    doc = nlp(text)

    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    education = [ent.text for ent in doc.ents if ent.label_ == "EDUCATION"]
    experience = [ent.text for ent in doc.ents if ent.label_ == "ORG"]

    return {
        "text": text,
        "skills": list(set(skills)),
        "education": list(set(education)),
        "experience": list(set(experience)),
    }
