import random
import string
from data_faker.web.dtos.person_info_dto import PersonInfoDTO
import json
from functools import cache
import re
from data_faker.db.enums import Gender


def generate_number() -> str:
    """Generate a random number between 1 and 999.
    A letter might be added at the end."""
    number = random.randint(1, 999)

    # Decide whether to append an uppercase letter
    if random.choice([True, False]):
        letter = random.choice(string.ascii_uppercase)
        return f"{number}{letter}"
    else:
        return str(number)


def generate_floor() -> str:
    """Generate a random floor number."""
    if random.randint(1, 100) <= 35:
        return "st"
    else:
        return str(random.randint(1, 99))


@cache
def extract_person_info(path: str) -> list[PersonInfoDTO]:
    """
    Extracts the first_name, last_name, and gender
    Returns:
        A list of PersonInfoDTOs.
    """
    with open(path, encoding="utf-16") as file:
        data = json.load(file)

        # Check if persons array exists and has at least one object
        is_valid = (
            "persons" in data
            and isinstance(data["persons"], list)
            and len(data["persons"]) > 0
        )

        if is_valid:
            persons_info = data["persons"]

            return [
                PersonInfoDTO(
                    name=person["name"],
                    surname=person["surname"],
                    gender=Gender(person["gender"]),
                )
                for person in persons_info
            ]

        raise FileNotFoundError("File does not exists")


def is_valid_name(name: str) -> bool:
    """
    Validates if the given name contains only English and Danish letters.
    """
    if name is None or not isinstance(name, str):
        raise ValueError("Value must be of type string")

    pattern = r"^[A-Za-zæøåÆØÅ\.]([A-Za-zæøåÆØÅ\. ]|-[^-]+|[^-]+-)*[A-Za-zæøåÆØÅ\.]$"
    return bool(re.match(pattern, name))


def is_valid_floor(s: str) -> bool:
    """Check if the floor generated is valid."""
    if s is None:
        raise ValueError("Value cannot be of type None")
    if s == "st":
        return True
    if s.isdigit() and 1 <= int(s) <= 99:
        return True
    return False


def is_valid_number(s: str) -> bool:
    """Check if the number generated is valid."""
    if s is None or not isinstance(s, str):
        raise ValueError("Value must be of type string")
    if s.isdigit() and 1 <= int(s) <= 999:
        return True
    if s[-1] in string.ascii_uppercase and s[:-1].isdigit() and 1 <= int(s[:-1]) <= 999:
        return True
    return False


def is_valid_street(name: str) -> bool:
    """Check if the street name generated is valid."""
    if name is None or not isinstance(name, str):
        raise ValueError("Value must be of type string")
    pattern = r"^[A-Za-zæøåÆØÅ\.][A-Za-zæøåÆØÅ\. ]*[A-Za-zæøåÆØÅ\.]$"

    return bool(re.match(pattern, name))
