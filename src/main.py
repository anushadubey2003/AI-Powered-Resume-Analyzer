from parser import parse_resume
from scorer import rule_based_score, semantic_similarity
from db import save_resume_data

with open("data/job_description.txt", "r") as f:
    job_desc = f.read()
    keywords = job_desc.split()

resume_data = parse_resume("data/sample_resume.pdf")
rule_score = rule_based_score(resume_data, keywords)
semantic_score = semantic_similarity(resume_data["text"], job_desc)

resume_data["rule_score"] = rule_score
resume_data["semantic_score"] = semantic_score

save_resume_data("resume_001", resume_data)

print("Rule Score:", rule_score)
print("Semantic Score:", semantic_score)
