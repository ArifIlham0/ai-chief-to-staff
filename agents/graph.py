from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END

class ChiefState(TypedDict):
    objective: str
    plan: List[str]
    research: Dict
    rag_findings: Dict
    browser_findings: Dict
    analysis: Dict
    draft_report: str
    final_report: str
    review_notes: str