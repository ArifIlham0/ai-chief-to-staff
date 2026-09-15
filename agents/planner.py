from tools.llm_tool import ask_llm
from memory.memory_store import get_memory, save_memory

def planner_agent(state):
    topic = state["topic"]
    memory = get_memory(topic)
    
    prompt = f"""
You are a research planning agent.

Research topic:
{topic}

Relevant memory:
{memory}

Create a practical 5-step research plan.
Return only numbered steps.
"""

    plan_text = ask_llm(prompt)

    plan = [
        line.strip()
        for line in plan_text.split("\n")
        if line.strip()
    ]

    save_memory(topic, "plan", plan_text)

    state["memory"] = memory
    state["plan"] = plan

    return state