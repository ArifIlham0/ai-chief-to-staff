from tools.llm_tool import ask_llm
from memory.memory_store import save_memory

def reflector_agent(state):
    topic = state["topic"]
    draft_report = state["draft_report"]

    prompt = f"""
You are a critical reviewer.

Review this research report for:
- Missing information
- Weak reasoning
- Unsupported claims
- Poor structure
- Unclear recommendations

Topic:
{topic}

Draft report:
{draft_report}

Return:
1. Review notes
2. Improved final report
"""

    review = ask_llm(prompt)

    save_memory(topic, "reflection", review)

    state["reflection_notes"] = review
    state["final_report"] = draft_report + "\n\n---\n\nReflection Review:\n"

    return state