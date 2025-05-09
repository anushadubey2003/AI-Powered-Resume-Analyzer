from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def rule_based_score(resume_data, job_keywords):
    match_count = sum(1 for kw in job_keywords if kw.lower() in resume_data["text"].lower())
    return (match_count / len(job_keywords)) * 100

def semantic_similarity(resume_text, job_description):
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_description, convert_to_tensor=True)
    score = util.pytorch_cos_sim(emb1, emb2)
    return float(score[0][0]) * 100
