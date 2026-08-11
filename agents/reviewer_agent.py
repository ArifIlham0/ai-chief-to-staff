def reviewer_agent(state):
    report = state["draft_report"]

    review_notes = []

    if "Objective" not in report:
        review_notes.append("Missing Objective Section")

    if "Recommendation" not in report:
        review_notes.append("Missing Recommendation Section")

    if len(report) < 1000:
        review_notes.append("Report may be too short")

    if not review_notes:
        review_notes.append("Report passed basic quality checks")

    state["review_notes"] = "\n".join(review_notes)
    state["final_report"] = report + "\n\n## Review Notes\n" + state["review_notes"]

    return state