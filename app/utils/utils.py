def is_header_line(*, line: str, lookup: str) -> bool:
    if line.strip().lower() == lookup.strip().lower():
        return True
    return False


def convert_str_to_bool(value: str) -> bool:
    if value.strip().lower() == "true":
        return True
    else:
        return False
