import json
import os.path
from config import ROOT_DIR
from datetime import datetime


OPERATION_PATH = os.path.join(ROOT_DIR, "data", "operations.json")


def get_list_json():
    with open(OPERATION_PATH, encoding="utf-8") as file:
        result = json.load(file)
        return result


def filter_list_json():
    filter_list = []
    for state in get_list_json():
        if state.get("state") == "EXECUTED":
            filter_list.append(state)
    return filter_list


def sort_result_json():
    return sorted(filter_list_json(), key=lambda x: x['date'], reverse=True)


def take_operations():
    return sort_result_json()[:5]


def format_date(date):
    datetime_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return datetime_date.strftime("%d.%m.%Y")


def mask_number(number):
    number_list = number.split(" ")
    number_for_format = number_list[-1]
    if number_list[0] == "Счет":
        format_number = f"**{number_for_format[-4:]}"
        number_list[-1] = format_number
        return " ".join(number_list)
    elif number_list[0] == "":
        return "Вклад"
    else:
        format_number = f"{number_for_format[:4]} {number_for_format[4:6]}** **** {number_for_format[-4:]}"
        number_list[-1] = format_number
        return " ".join(number_list)


def print_result():
    for operation in take_operations():
        date = format_date(operation['date'])
        description = operation['description']
        from_account = mask_number(operation.get('from', ''))
        to_account = mask_number(operation.get('to', ''))
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f"{date} {description}\n{from_account} -> {to_account}\n{amount} {currency}\n")

