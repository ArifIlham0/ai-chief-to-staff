async function runAgent() {
    const objective = document.getElementById("objective").value;
    const status = document.getElementById("status");
    const report = document.getElementById("report");

    status.textContent = "Running agents...";

    const response = await fetch("http://localhost:8000/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ objective })
    });

    const data = await response.json();

    status.textContent = JSON.stringify({
        plan: data.plan,
        review_notes: data.review_notes,
        markdown_report: data.markdown_report,
        pdf_report: data.pdf_report
    }, null, 2);

    report.textContent = data.final_report;
}