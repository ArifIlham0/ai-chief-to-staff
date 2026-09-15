from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import TaskRequest
from agents.graph import run_chief_of_staff
from reports.report_generator import save_markdown_report, save_pdf_report
from pydantic import BaseModel
from agents.graph import run_research_agent

# app = FastAPI(title="AI Chief of Staff")
app = FastAPI(title="Autonomous Research Agent")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def home():
#     return {
#         "message": "AI Chief of Staff is running"
#     }

# @app.post("/run")
# def run_task(request: TaskRequest):
#     result = run_chief_of_staff(request.objective)

#     markdown_path = save_markdown_report(result["final_report"])
#     pdf_path = save_pdf_report(result["final_report"])
    
#     result["markdown_report"] = markdown_path
#     result["pdf_report"] = pdf_path

#     return result

class ResearchRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {
        "message": "Autonomous Research Agent is running"
    }

@app.post("/research")
def research(request: ResearchRequest):
    result = run_research_agent(request.topic)

    return {
        "topic": result["topic"],
        "plan": result["plan"],
        "findings": result["findings"],
        "reflection_notes": result["reflection_notes"],
        "final_report": result["final_report"],
        "output_path": result["output_path"]
    }