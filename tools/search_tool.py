def search_web_simulated(query: str):
    return [
        {
            "title": "AI Agents Overview",
            "source": "internal-demo-source",
            "summary": f"AI agents use planning, reasoning, tools, and memory to complete goals related to: {query}"
        },
        {
            "title": "RAG and Agents Workflows",
            "source": "internal-demo-source",
            "summary": f"RAG improves AI reliability by retrieving relevant knowledge before generating responses."
        },
        {
            "title": "Tool Calling in AI Systems",
            "source": "internal-demo-source",
            "summary": "Tool calling allows AI systems to interact with APIs, databases, files, and external services."
        }
    ]