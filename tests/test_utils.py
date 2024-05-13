from src.utils import (get_list_json, filter_list_json, sort_result_json,
                       format_date, mask_number, get_result)


def test_get_list_json():
    data = get_list_json()
    assert data is not None
    assert type(data) == list


def test_filter_list_json(operations):
    assert filter_list_json(operations) == [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]


def test_sort_result_json(operations):
    date = sort_result_json(operations)
    dates = [operation['date'] for operation in date]
    assert dates == ["2020-06-30T02:08:58.425572", "2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364"]


def test_format_date():
    assert format_date("2019-07-03T18:35:29.512364") == "03.07.2019"


def test_mask_number():
    assert mask_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_number("Счет 64686473678894779589") == "Счет **9589"


def test_get_result(operations):
    assert get_result(operations) == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n',
                                      '03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD\n',
                                      '30.06.2020 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD\n']
