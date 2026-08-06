from pydantic import BaseModel

class TaskRequest(BaseModel):
    objective: str

class TaskResponse(BaseModel):
    objective: str
    plan: list
    review_notes: str
    final_report: str
    markdown_report: str | None = None
    pdf_report: str | None = None