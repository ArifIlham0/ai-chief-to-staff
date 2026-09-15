from tools.search_tool import search_web_simulated
from tools.calculator_tool import calculate_relevance_score
from memory.memory_store import save_memory

def executor_agent(state):
    topic = state["topic"]

    search_results = search_web_simulated(topic)

    enriched_findings = []

    for item in search_results:
        score = calculate_relevance_score(
            importance=8,
            confidence=7,
            risk=2
        )

        enriched_findings.append({
            "title": item["title"],
            "source": item["source"],
            "summary": item["summary"],
            "relevance_score": score,
        })

    save_memory(topic, "findings", str(enriched_findings))

    state["findings"] = enriched_findings

    return state