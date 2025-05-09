from pymongo import MongoClient

def save_resume_data(resume_id, data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["resume_db"]
    resumes = db["resumes"]
    data["_id"] = resume_id
    resumes.replace_one({"_id": resume_id}, data, upsert=True)
