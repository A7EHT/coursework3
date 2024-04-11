import json
import os.path
from config import ROOT_DIR


OPERATION_PATH = os.path.join(ROOT_DIR, "data", "operations.json")
def get_list_json():
    with open("../data/operations.json", encoding="utf-8") as file:
        result = json.load(file)
        return result


