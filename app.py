from fastapi import FastAPI
from scoring_engine import analyze_company

app = FastAPI(title="Zeutara Execution-Strain Engine")

@app.get("/")
def home():
    return {"message": "Zeutara Execution-Strain Engine is running"}

@app.post("/analyze")
def analyze(data: dict):
    return analyze_company(data)
