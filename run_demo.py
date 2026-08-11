from rag.ingest import ingest_documents
from agents.graph import run_chief_of_staff
from reports.report_generator import save_markdown_report, save_pdf_report

if __name__ == "__main__":
    objective = "Analyze the AI coding assistant market"

    print("Ingesting internal documents...")
    ingest_documents()

    print("Running AI Chief of Staff...")
    result = run_chief_of_staff(objective)

    print("Saving report...")
    markdown_path = save_markdown_report(result["final_report"])
    pdf_path = save_pdf_report(result["final_report"])

    print("\nAI Chief of Staff Complete")
    print("--------------------------------")
    print(f"Objective: {result['objective']}")
    print(f"Markdown Report: {markdown_path}")
    print(f"PDF Report: {pdf_path}")
    print("\nReview Notes:")
    print(result["review_notes"])