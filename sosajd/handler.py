import json

def function_one(event, context):
    body = {
        "name": "Jd",
        "last_name": "Abarka",
        "age": 22,
        "student_code": 240220222029,
        "birth_place": "leticia",
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def function_two(event, context):
    body = {
        "name": "THE Sosa",
        "last_name": "Sosa",
        "age": 21,
        "student_code": 240220222016,
        "birth_place": "armenia",
        "girlfriend_name": "aleja",
        "girlfriend_last_name": "mejia",
        "hobby": "soccer, penis",
        "favorite_color": "red",
        "best_movie": "bee movie",
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response