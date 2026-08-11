import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def save_markdown_report(content, filename="executive_report.md"):
    os.makedirs("./data/outputs", exist_ok=True)
    path = f"./data/outputs/{filename}"

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    return path

def save_pdf_report(content, filename="executive_report.pdf"):
    os.makedirs("./data/outputs", exist_ok=True)
    path = f"./data/outputs/{filename}"

    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    y = height - 40

    for line in content.split("\n"):
        if y < 40:
            c.showPage()
            y = height - 40

        c.drawString(40, y, line[:100])
        y -= 14

    c.save()

    return path