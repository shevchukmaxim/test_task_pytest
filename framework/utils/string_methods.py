import re


def remove_references(string: str) -> str:
    return re.sub(r'\[\d+\]', '', string)


def remove_text_in_brackets(string: str) -> str:
    return re.sub(r'\s?\(.*?\)', '', string)


def remove_extra_details_from_string(string: str) -> str:
    string = remove_references(string)
    string = remove_text_in_brackets(string)
    return string


def convert_string_with_punctuation_into_int(string: str) -> int:
    return int(re.sub(r'[.,]', '', string))
