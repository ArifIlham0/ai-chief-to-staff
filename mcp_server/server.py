from mcp.server.fastmcp import FastMCP
from mcp_server.tools import calculate_score, save_report, get_current_date

mcp = FastMCP("AI Chief of Staff MCP Server")

@mcp.tool()
def competitor_score(features: int, enterprise: int, risk: int) -> float:
    return calculate_score(features, enterprise, risk)

@mcp.tool()
def write_report(filename: str, content: str) -> dict:
    return save_report(filename, content)

@mcp.tool()
def current_date() -> str:
    return get_current_date()

if __name__ == "__main__":
    mcp.run()