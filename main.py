from src.utils import get_list_json, filter_list_json, sort_result_json, get_result


def main():
    data = get_list_json()
    filter_data = filter_list_json(data)
    sort_result = sort_result_json(filter_data)
    result = get_result(sort_result)
    for string in result:
        print(string)


if __name__ == "__main__":
    main()