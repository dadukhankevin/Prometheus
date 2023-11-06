import json

def is_valid_json(my_string):
    try:
        json.loads(my_string)
        return True
    except ValueError:
        return False