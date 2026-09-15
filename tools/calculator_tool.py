def calculate_relevance_score(importance: int, confidence: int, risk: int):
    return round((importance * 0.4) + (confidence * 0.4) - (risk * 0.2), 2)