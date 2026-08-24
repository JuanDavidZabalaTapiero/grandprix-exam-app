import re


def normalize_text(value):
    if value:
        value = value.strip()
        value = re.sub(r"\s+", " ", value)
        return value.upper()
    return value
