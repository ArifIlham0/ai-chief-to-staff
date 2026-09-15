from tools.file_tool import save_text_file

def save_final_report(state):
    topic = state["topic"]

    safe_topic = topic.lower().replace(" ", "_").replace("/", "_")
    filename = f"{safe_topic}_research_agent.md"

    path = save_text_file(filename, state["final_report"])

    state["output_path"] = path

    return state