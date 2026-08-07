def research_agent(state):
    objective = state["objective"]

    state["research"] = {
        "objective": objective,
        "competitors": [
            "OpenAI Codex",
            "Claude Code",
            "GitHub Copilot",
            "IBM Bob",
            "Cursor",
        ],
        "research_questions": [
            "What does each tool do?",
            "Who is the target audience?",
            "What enterprise capabilities exist?",
            "What risk of limitation exist?",
            "Which tool is strongest for enterprise use?",
        ]
    }