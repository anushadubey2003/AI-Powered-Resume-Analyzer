from src.main import parse_resume, rule_based_score, semantic_similarity, save_resume_data

def lambda_handler(event, context):
    file_path = event["file_path"]
    job_desc = event["job_description"]
    resume_id = event["resume_id"]

    resume_data = parse_resume(file_path)
    keywords = job_desc.split()
    resume_data["rule_score"] = rule_based_score(resume_data, keywords)
    resume_data["semantic_score"] = semantic_similarity(resume_data["text"], job_desc)

    save_resume_data(resume_id, resume_data)

    return {
        "statusCode": 200,
        "body": {
            "rule_score": resume_data["rule_score"],
            "semantic_score": resume_data["semantic_score"]
        }
    }
