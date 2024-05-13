import json
from config import OPERATION_PATH
from datetime import datetime


def get_list_json():
    """Берем список словарей из файла json"""
    with open(OPERATION_PATH, encoding="utf-8") as file:
        result = json.load(file)
        return result


def filter_list_json(result):
    """Фильтруем список по статусу EXECUTED"""
    filter_list = []
    for state in result:
        if state.get("state") == "EXECUTED":
            filter_list.append(state)
    return filter_list


def sort_result_json(filter_list):
    """Выполняем сортировку, чтобы последние операции по дате были в начале списка"""
    """Берем срез последних 5-ти операций"""
    sort_filter_list = sorted(filter_list, key=lambda x: x['date'], reverse=True)[:5]
    return sort_filter_list


def format_date(date):
    """Меняем дату, по требованию задания"""
    datetime_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return datetime_date.strftime("%d.%m.%Y")


def mask_number(number):
    """Осуществляем шифрование"""
    number_list = number.split(" ")
    number_for_format = number_list[-1]
    if number_list[0] == "Счет":
        format_number = f"**{number_for_format[-4:]}"
        number_list[-1] = format_number
        return " ".join(number_list)
    elif number_list[0] == "":
        return "Наличные"
    else:
        format_number = f"{number_for_format[:4]} {number_for_format[4:6]}** **** {number_for_format[-4:]}"
        number_list[-1] = format_number
        return " ".join(number_list)


def get_result(sort_filter_list):
    operation_list = []
    for operation in sort_filter_list:
        date = format_date(operation['date'])
        description = operation['description']
        from_account = mask_number(operation.get('from', ''))
        to_account = mask_number(operation.get('to', ''))
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        operation_list.append(f"{date} {description}\n{from_account} -> {to_account}\n{amount} {currency}\n")
    return operation_list
