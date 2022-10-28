def list_to_string(list: list) -> str:
    return ''.join(list)


def string_to_list(string: str) -> list:
    if not isinstance(string, str):
        raise TypeError

    return list(string)
