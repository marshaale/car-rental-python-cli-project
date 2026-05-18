def is_header_line(*, line: str, lookup: str) -> bool:
    if line.strip().lower() == lookup.strip().lower():
        return True
    return False
