def write_agent(state):
    objective = state["objective"]
    analysis = state["analysis"]
    rag = state["rag_findings"]
    browser = state["browser_findings"]

    report = f"""
# AI Chief of Staff Executive Report

## Objective

{objective}

## Plan

{chr(10).join("- " + item for item in state["plan"])}

## Internal Knowledge Findings
"""

    for item in rag["results"]:
        report += f"""
### Source: {item["source"]}

{item["content"][:500]}
"""
    report += """

## External Browser Research
"""

    for source in browser["sources"]:
        report += f"""
### {source.get("title", "Unknown")}

URL: {source.get("url")}

Summary:
{source.get("text", source.get("error", "Unknown Error"))[:700]}
"""

    report += """

## Competitor Analysis
"""

    for name, details in analysis["competitor_analysis"].items():
        report += f"""
### {name}

- Capability Score: {details["capability_score"]}
- Enterprise Score: {details["enterprise_score"]}
- Risk Score: {details["risk_score"]}
- Overall Score: {details["overall_score"]}
- Summary: {details["summary"]}
"""

    report += f"""

## Recommendation

{analysis["recommendation"]}
"""

    state["draft_report"] = report

    return state