import json


def calculate_highest_type(questions):
    types = {}
    for question in questions:
        question_type = question.get("type")
        points = question.get("points")
        if question_type in types:
            types[question_type] += points
        else:
            types[question_type] = points
    highest_type = max(types, key=types.get)
    return highest_type

# Example usage
questions = [
    {
        "question": "Como você prefere resolver problemas?",
        "answer": "Explicando em palavras",
        "type": "Linguístico",
        "points": 3,
        "question_number": 1
    },
    {
        "question": "O que você prefere fazer nas horas vagas?",
        "answer": "Ler ou escrever",
        "type": "Linguístico",
        "points": 2,
        "question_number": 2
    }
]

highest_type = calculate_highest_type(questions)
print(f"The type with the highest points is: {highest_type}")