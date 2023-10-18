import re
import string


def is_valid_name(name: str) -> bool:
    """
    Validates if the given name contains only English and Danish letters.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    # Regular expression pattern to match only English and Danish letters and spaces, but not starting or ending spaces.
    pattern = r"^[A-Za-zæøåÆØÅ\.][A-Za-zæøåÆØÅ\. ]*[A-Za-zæøåÆØÅ\.]$"

    return bool(re.match(pattern, name))


def is_valid_floor(s: str) -> bool:
    if s == "st":
        return True
    if s.isdigit() and 1 <= int(s) <= 99:
        return True
    return False


def is_valid_number(s: str) -> bool:
    if s.isdigit() and 1 <= int(s) <= 999:
        return True
    if s[-1] in string.ascii_uppercase and s[:-1].isdigit() and 1 <= int(s[:-1]) <= 999:
        return True
    return False
