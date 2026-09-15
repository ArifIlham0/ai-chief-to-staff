from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from agents.knowledge_agent import knowledge_agent
from agents.research_agent import research_agent
from agents.reviewer_agent import reviewer_agent
from agents.analyst_agent import analyst_agent
from agents.browser_agent import browser_agent
from agents.chief_agent import chief_planner
from agents.writer_agent import writer_agent
from agents.writer import writer_agent as research_writer_agent
from memory.memory_store import init_memory
from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.reflector import reflector_agent
from reports.report_writer import save_final_report

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

class ResearchState(TypedDict):
    topic: str
    memory: List[Dict]
    plan: List[str]
    findings: List[Dict]
    draft_report: str
    reflection_notes: str
    final_report: str
    output_path: str

def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("planner", planner_agent)
    graph.add_node("executor", executor_agent)
    graph.add_node("writer", research_writer_agent)
    graph.add_node("reflector", reflector_agent)
    graph.add_node("save_report", save_final_report)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "writer")
    graph.add_edge("writer", "reflector")
    graph.add_edge("reflector", "save_report")
    graph.add_edge("save_report", END)

    return graph.compile()

def run_research_agent(topic: str):
    init_memory()

    app = build_research_graph()

    initial_state = {
        "topic": topic,
        "memory": [],
        "plan": [],
        "findings": [],
        "draft_report": "",
        "reflection_notes": "",
        "final_report": "",
        "output_path": ""
    }

    return app.invoke(initial_state)