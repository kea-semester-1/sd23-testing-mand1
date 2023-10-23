import pytest
from data_faker.db.dao.address_dao import AddressDAO
from sqlalchemy.ext.asyncio import AsyncSession

from data_faker.db import mo_utils as utils


@pytest.mark.anyio
async def test_address_dao_returning_correct_amount_of_rows(
    dbsession: AsyncSession, address_data: None
) -> None:
    """Test for adr."""

    amount_of_rows = 10
    address_dao = AddressDAO(dbsession)
    address = await address_dao.get_random_row(amount_of_rows)

    assert address
    assert len(address) == amount_of_rows


@pytest.mark.anyio
async def test_address_dao_returning_valid_postal_code(
    dbsession: AsyncSession, address_data: None
) -> None:
    """Test if address dao returns valid postal_code."""

    address_dao = AddressDAO(dbsession)
    address = await address_dao.get_random_row()

    assert utils.is_valid_postal_code(address[0].postal_code)


@pytest.mark.anyio
async def test_address_dao_returning_valid_town_name(
    dbsession: AsyncSession, address_data: None
) -> None:
    """Test if address dao returns valid town name."""

    address_dao = AddressDAO(dbsession)
    address = await address_dao.get_random_row()

    assert utils.is_valid_town_name(address[0].town)


@pytest.mark.parametrize(
    "postal_code, expected",
    [
        (4000, True),
        (1234, True),
        (6789, True),
        ("4000#", False),
        ("40AB2", False),
        (302, False),
        (40001, False),
    ],
)
def test_postal_code_validation(postal_code: int, expected: bool) -> None:
    """Test for validating postal_code."""
    assert utils.is_valid_postal_code(postal_code) == expected


@pytest.mark.parametrize(
    "town_name, expected",
    [
        # Valid town names
        ("København", True),
        ("Frederiksberg C", True),
        ("Aarhus", True),
        ("Odense", True),
        # Invalid names - names with numbers
        ("København1", False),
        # Invalid names - special characters not belonging to Danish
        ("København@", False),
        ("Odense!", False),
        # Invalid names - characters from another language
        ("Københavnגבעת", False),  # Hebrew character mixed
        ("OdenseСолн", False),  # Russian character mixed
        # Invalid names - only spaces
        ("   ", False),
        # Names with leading or trailing spaces but are still valid
        (" København", True),
        ("Odense ", True),
        # Empty names
        ("", False),
    ],
)
def test_is_valid_town_name(town_name: str, expected: bool) -> None:
    """Test for valid town name."""
    assert utils.is_valid_town_name(town_name) == expected
