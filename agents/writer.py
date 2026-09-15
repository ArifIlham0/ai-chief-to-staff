from tools.llm_tool import ask_llm
from memory.memory_store import save_memory

def writer_agent(state):
    topic = state["topic"]
    plan = state["plan"]
    findings = state["findings"]

    prompt = f"""
You are an expert research analyst.

Write a professional research report.

Topic:
{topic}

Research plan:
{plan}

Findings:
{findings}

Report structure:
1. Executive Summary
2. Key Findings
3. Analysis
4. Risks and Limitations
5. Recommendations
6. Conclusion

Write in a clear business style.
"""

    report = ask_llm(prompt)

    save_memory(topic, "draft_report", report)

    state["draft_report"] = report

    return state

    