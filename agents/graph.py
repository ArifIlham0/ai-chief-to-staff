from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from agents.knowledge_agent import knowledge_agent
from agents.research_agent import research_agent
from agents.reviewer_agent import reviewer_agent
from agents.analyst_agent import analyst_agent
from agents.browser_agent import browser_agent
from agents.chief_agent import chief_planner
from agents.writer_agent import writer_agent

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

def build_graph():
    graph = StateGraph(ChiefState)

    graph.add_node("chief_planner", chief_planner)
    graph.add_node("research_agent", research_agent)
    graph.add_node("knowledge_agent", knowledge_agent)
    graph.add_node("browser_agent", browser_agent)
    graph.add_node("analyst_agent", analyst_agent)
    graph.add_node("writer_agent", writer_agent)
    graph.add_node("reviewer_agent", reviewer_agent)

    graph.set_entry_point("chief_planner")

    graph.add_edge("chief_planner", "research_agent")
    graph.add_edge("research_agent", "knowledge_agent")
    graph.add_edge("knowledge_agent", "browser_agent")
    graph.add_edge("browser_agent", "analyst_agent")
    graph.add_edge("analyst_agent", "writer_agent")
    graph.add_edge("writer_agent", "reviewer_agent")
    graph.add_edge("reviewer_agent", END)

    return graph.compile()

def run_chief_of_staff(objective: str):
    app = build_graph()

    initial_state = {
        "objective": objective,
        "plan": [],
        "research": {},
        "rag_findings": {},
        "browser_findings": {},
        "analysis": {},
        "draft_report": "",
        "final_report": "",
        "review_notes": ""
    }

    result = app.invoke(initial_state)

    return {
        "objective": result["objective"],
        "plan": result["plan"],
        "review_notes": result["review_notes"],
        "final_report": result["final_report"]
    }