from mcp_server.tools import calculate_score

def analyst_agent(state):
    competitors = state["research"]["competitors"]

    analysis = {}

    for competitor in competitors:
        features = 8
        enterprise = 7
        risk = 3

        score = calculate_score(
            features=features,
            enterprise=enterprise,
            risk=risk,
        )

        analysis[competitor] = {
            "capability_score": features,
            "enterprise_score": enterprise,
            "risk_score": risk,
            "overall_score": score,
            "summary": f"{competitor} is evaluated across features, enterprise capabilities, and risk of limitation."
        }

    state["analysis"] = {
        "competitor_analysis": analysis,
        "recommendation": "Use different AI coding assistants based on enterprise needs.",
    }

    return state