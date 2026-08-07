from browser.web_runner import scrape_page

def browser_agent(state):
    urls = [
        "https://github.com/features/copilot",
        "https://claude.com/product/claude-code",
        "https://openai.com/codex/",
    ]

    findings = []

    for url in urls:
        try:
            findings.append(scrape_page(url))
        except Exception as error:
            findings.append({
                "url": url,
                "error": str(error),
            })

    state["browser_findings"] = {
        "sources": findings,
    }

    return state
