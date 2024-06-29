

def serializer(form_answer):
    return {
        "id": str(form_answer["_id"]),
        "question": form_answer["question"],
        "question_number": form_answer["question_number"],
        "answer": form_answer["answer"],
        "type": form_answer["type"],
        "form_id": form_answer["form_id"],
        "user": form_answer["user"],
        "points": form_answer["points"],
    }

def list_serializer(form_answers):
    return [serializer(form_answer) for form_answer in form_answers]