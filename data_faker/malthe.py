import random
import string
from data_faker.web.dtos.person_info_dto import PersonInfoDTO
import json
from functools import cache
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
