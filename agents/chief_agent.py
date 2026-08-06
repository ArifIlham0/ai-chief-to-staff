def chief_planner(state):
    objective = state["objective"]

    plan = [
        "Break down the business objective",
        "Search internal knowledge base",
        "Collect external market research",
        "Analyze competitors",
        "Generate executive report",
        "Review report for accuracy and clarity",
    ]

    state["plan"] = plan

    return state