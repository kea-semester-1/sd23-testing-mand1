import random
import re
from data_faker.db.dao.address_dao import AddressDAO
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data_faker.db.models.models import Address
from data_faker.db.dependencies import get_db_session
import asyncio


def generate_phone_number() -> str:
    """Generates a random unique phone number."""
    return "".join(str(random.randint(2, 7)) for _ in range(8))


def is_valid_phone_number(number: str) -> bool:
    """Checks if number is valid,."""
    valid_prefixes = [
        "2",
        "30",
        "31",
        "40",
        "41",
        "42",
        "50",
        "51",
        "52",
        "53",
        "60",
        "61",
        "71",
        "81",
        "91",
        "92",
        "93",
        "342",
        "344",
        "345",
        "346",
        "347",
        "348",
        "349",
        "356",
        "357",
        "359",
        "362",
        "365",
        "366",
        "389",
        "398",
        "431",
        "441",
        "462",
        "466",
        "468",
        "472",
        "474",
        "476",
        "478",
        "485",
        "486",
        "488",
        "489",
        "493",
        "494",
        "495",
        "496",
        "498",
        "499",
        "542",
        "543",
        "545",
        "551",
        "552",
        "556",
        "571",
        "572",
        "573",
        "574",
        "577",
        "579",
        "584",
        "586",
        "587",
        "589",
        "597",
        "598",
        "627",
        "629",
        "641",
        "649",
        "658",
        "662",
        "663",
        "664",
        "665",
        "667",
        "692",
        "693",
        "694",
        "697",
        "771",
        "772",
        "782",
        "783",
        "785",
        "786",
        "788",
        "789",
        "826",
        "827",
        "829",
    ]

    pattern = (
        "^(?:"
        + "|".join([f"{prefix}\\d{{{8 - len(prefix)}}}" for prefix in valid_prefixes])
        + ")$"
    )

    return bool(re.match(pattern, number))


def get_valid_phone_number() -> str:
    """Returns a valid phone_number."""
    phone_number = generate_phone_number()

    if not is_valid_phone_number(phone_number):
        return get_valid_phone_number()

    return phone_number


def get_address_dao(session: AsyncSession = Depends(get_db_session)) -> AddressDAO:
    return AddressDAO(session)


async def get_random_postal_code_and_town(
    limit: int,
    address_dao: AddressDAO = Depends(get_address_dao),
) -> Address:
    address = await address_dao.get_random_row(limit=limit)
    return address
