from rag.retriever import retrieve_knowledge

def knowledge_agent(state):
    objective = state["objective"]

    findings = retrieve_knowledge(objective)

    state["rag_findings"] = {
        "query": objective,
        "results": findings,
    }
    return state