import os

def save_text_file(filename: str, content: str):
    os.makedirs("data/outputs", exist_ok=True)

    path = f"data/outputs/{filename}"

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    return path