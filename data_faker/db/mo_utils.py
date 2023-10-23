import random
import re
from data_faker.db.dao.address_dao import AddressDAO
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data_faker.db.dependencies import get_db_session
from data_faker.constants import VALID_PHONE_PREFIXES
import string


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


def get_address_dao(session: AsyncSession = Depends(get_db_session)) -> AddressDAO:
    """Get address dao."""
    return AddressDAO(session)


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
