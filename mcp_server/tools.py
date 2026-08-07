import os
import datetime

def calculate_score(features, enterprise, risk):
    return round((features * 0.4) + (enterprise * 0.4) - (risk * 0.2), 2)

def save_report(filename, content):
    os.makedirs("./data/outputs", exist_ok=True)
    path = f"./data/outputs/{filename}"

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    return {
        "saved_to": path,
    }

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")