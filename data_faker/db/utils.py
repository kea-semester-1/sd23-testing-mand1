import json
import random
import re
from datetime import datetime, timedelta
from functools import cache

from faker import Faker

from data_faker import constants
from data_faker.constants import VALID_PHONE_PREFIXES
import string

from data_faker.db.enums import Gender
from data_faker.web.dtos.person_info_dto import PersonInfoDTO

fake = Faker("da_Dk")


def generate_phone_number() -> str:
    """Generates a random unique phone number."""
    return "".join(str(random.randint(2, 7)) for _ in range(8))


def is_valid_phone_number(number: str) -> bool:
    """Checks if phone_number is valid."""

    if number is None:
        return False

    pattern = (
        "^(?:"
        + "|".join(
            [f"{prefix}\\d{{{8 - len(prefix)}}}" for prefix in VALID_PHONE_PREFIXES]
        )
        + ")$"
    )

    return bool(re.match(pattern, number))


def generate_valid_phone_number() -> str:
    """Returns a valid phone_number."""
    phone_number = generate_phone_number()

    if not is_valid_phone_number(phone_number):
        return generate_valid_phone_number()

    return phone_number


def is_valid_postal_code(postal_code: int) -> bool:
    """Check if value is valid."""
    return bool(re.match(r"^\d{4}$", str(postal_code)))


def is_valid_town_name(town_name: str) -> bool:
    """Validates if a given town name is a valid Danish town name."""

    if not town_name:
        return False

    town_name = town_name.strip()

    # allows for spaces between words in town names, e.g., "Frederiksberg C"
    pattern = re.compile(r"^[a-zA-ZæøåÆØÅ\s]+$")

    return bool(pattern.match(town_name))


def generate_door_value() -> str:
    """Generate random door value.

    choice 1: Return "th", "mf", or "tv".
    choice 2: Return a number from 1 to 50.
    choice 3: Return a lowercase letter optionally followed by a dash,
              then followed by one to three numeric digits.
    """
    choice = random.randint(1, 3)

    if choice == 1:
        return random.choice(["th", "mf", "tv"])

    if choice == 2:
        return str(random.randint(1, 50))

    letter = random.choice(string.ascii_lowercase)
    dash = "-" if random.choice([True, False]) else ""
    number = str(random.randint(1, 999))
    return f"{letter}{dash}{number}"


def is_valid_door_value(value: str) -> bool:
    """Validate the format of the door value."""

    if not value:
        return False

    if value in ["th", "mf", "tv"]:
        return True

    # Check for a number from 1 to 50
    if re.match(r"^[1-9]$|^[1-4][0-9]$|^50$", value):
        return True

    # Check for a lowercase letter optionally followed by a dash,
    # then followed by one to three numeric digits
    if re.match(r"^[a-z](-?\d{1,3})$", value):
        return True

    return False


def generate_valid_door_value() -> str:
    """Generates a valid door value."""
    door = generate_door_value()

    if not is_valid_door_value(door):
        return generate_valid_door_value()

    return door


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


def generate_valid_street() -> str:
    """Generates a valid street name."""
    street = str(fake.street_name())

    if not is_valid_street(street):
        return generate_valid_street()

    return street


SEVENTH_CIPHER_MAPPING = {
    0: [(1900, 1999)],
    1: [(1900, 1999)],
    2: [(1900, 1999)],
    3: [(1900, 1999)],
    4: [(1937, 1999), (2000, 2036)],
    5: [(1858, 1899), (2000, 2057)],
    6: [(1858, 1899), (2000, 2057)],
    7: [(1858, 1899), (2000, 2057)],
    8: [(1858, 1899), (2000, 2057)],
    9: [(1937, 1999), (2000, 2036)],
}


def generate_seventh_cipher_range(year: str) -> list[str]:
    """Get a range of valid seventh ciphers, based on the year of birth."""
    return [
        str(key)
        for key, value in SEVENTH_CIPHER_MAPPING.items()
        if any(min_val <= int(year) <= max_val for min_val, max_val in value)
    ]


def validate_cpr_format(cpr: str) -> bool:
    """Validate the format of a CPR number."""

    invalid_input = cpr is None or not isinstance(cpr, str)

    if invalid_input:
        raise ValueError("Invalid input.")

    if len(cpr) != 10:
        raise ValueError(f"Invalid CPR number length. Length: {len(cpr)} ")

    if not cpr.isdigit():
        raise ValueError("Non-digit characters in CPR number.")

    dob = cpr[:6]
    date_format = "%d%m%y"

    try:
        datetime.strptime(dob, date_format)
    except ValueError as e:
        raise e

    return True


def validate_gender_match(cpr: str, gender: Gender) -> bool:
    """
    Validate if the gender matches the CPR number.

    If male: last cipher is odd
    If female: last cipher is even
    """

    if gender is None or cpr is None:
        raise ValueError("Invalid input.")

    if len(cpr) != 10:
        raise ValueError(f"Invalid CPR number length. Length: {len(cpr)} ")

    last_cipher_is_even = int(cpr[-1]) % 2 == 0

    gender_mismatch = (
        last_cipher_is_even
        and gender == Gender.male
        or not last_cipher_is_even
        and gender == Gender.female
    )

    if gender_mismatch:
        raise ValueError(f"Gender mismatch. gender: {gender}, last cipher: {cpr[-1]}")

    return True


def validate_seventh_cipher(cpr: str, full_year: str) -> bool:
    """Validate the seventh cipher of a CPR number."""
    seventh_cipher = cpr[6]
    valid_range = generate_seventh_cipher_range(full_year)

    if seventh_cipher not in valid_range:
        raise ValueError(
            f"Invalid seventh cipher. Cipher: {seventh_cipher},"
            f"year: {full_year}, range: {valid_range}",
        )

    return True


def generate_random_last_cipher(gender: Gender) -> str:
    """Generate the last cipher, based on gender."""

    return (
        str(random.choice([1, 3, 5, 7, 9]))
        if gender == Gender.male
        else str(random.choice([0, 2, 4, 6, 8]))
    )


def generate_cpr(date_of_birth: datetime, gender: Gender) -> str:
    """Generate a CPR number based on date of birth and gender."""

    invalid_input = (
        date_of_birth is None
        or gender is None
        or not isinstance(date_of_birth, datetime)
        or not isinstance(gender, Gender)
    )

    if invalid_input:
        raise ValueError("Invalid input.")

    invalid_date_range = (
        date_of_birth.year < constants.MIN_CPR_BIRTH_YEAR
        or date_of_birth.year > constants.MAX_CPR_BIRTH_YEAR
    )

    if invalid_date_range:
        raise ValueError(
            f"Cannot generate CPR-Number for birth years"
            f" less than {constants.MIN_CPR_BIRTH_YEAR}"
            f" or greater than {constants.MAX_CPR_BIRTH_YEAR}",
        )

    day = f"{date_of_birth.day:02}"
    month = f"{date_of_birth.month:02}"
    year = str(date_of_birth.year)
    year_short = year[-2:]

    seventh_cipher = random.choice(generate_seventh_cipher_range(year))
    eighth_cipher = random.randrange(0, 9)
    ninth_cipher = random.randrange(0, 9)
    last_cipher = generate_random_last_cipher(gender)

    dob_ciphers = f"{day}{month}{year_short}"
    control_ciphers = f"{seventh_cipher}{eighth_cipher}{ninth_cipher}{last_cipher}"
    return f"{dob_ciphers}-{control_ciphers}"


#######
# DOB #
#######


def generate_random_date_of_birth() -> datetime:
    """Generate a random date of birth."""
    start_date = datetime(constants.MIN_CPR_BIRTH_YEAR, 1, 1)
    end_date = datetime(constants.MAX_CPR_BIRTH_YEAR, 12, 31)
    days_between_dates = (end_date - start_date).days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)


def validate_date_format(date: datetime) -> bool:
    """Validate a date of birth."""

    if date is None or not isinstance(date, datetime):
        raise ValueError("Invalid input.")

    invalid_date_range = (
        date.year < constants.MIN_CPR_BIRTH_YEAR
        or date.year > constants.MAX_CPR_BIRTH_YEAR
    )

    if invalid_date_range:
        raise ValueError("Invalid date range.")

    return True
