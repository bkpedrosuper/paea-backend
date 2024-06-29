

def serializer(form):
    return {
        "id": str(form["_id"]),
        "name": form["name"],
    }

def list_serializer(forms):
    return [serializer(form) for form in forms]