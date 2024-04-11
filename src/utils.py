import json
import os.path
from config import ROOT_DIR


OPERATION_PATH = os.path.join(ROOT_DIR, "data", "operations.json")


def get_list_json():
    with open("../data/operations.json", encoding="utf-8") as file:
        result = json.load(file)
        return result


def filter_list_json():
    filter_list = []
    for state in get_list_json():
        if state["state"] == "EXECUTED":
            filter_list.append(state)
    return filter_list


def sort_result_json():
    return sorted(filter_list_json(), key=lambda x: x['date'], reverse=True)



