import json



def get_list_json():
    with open("operations.json") as file:
        data = json.loads(file)
        return data

