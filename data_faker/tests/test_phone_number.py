from data_faker.db.mo_utils import is_valid_phone_number
from data_faker.constants import VALID_PHONE_PREFIXES
import pytest


@pytest.mark.parametrize("prefix", VALID_PHONE_PREFIXES)
def test_valid_phone_numbers_lower_boundary(prefix: list[str]) -> None:
    """Test a valid phone number for lower boundary partition."""
    number = str(prefix) + "0" * (8 - len(prefix))
    assert is_valid_phone_number(number)


@pytest.mark.parametrize("prefix", VALID_PHONE_PREFIXES)
def test_valid_phone_numbers_upper_boundary(prefix: str) -> None:
    """Test a valid phone number for upper boundary partition."""
    number = prefix + "9" * (8 - len(prefix))
    assert is_valid_phone_number(number)


invalid_numbers = [
    # Numbers less than 8 digits
    "3000000",
    # Numbers more than 8 digits
    "300000000",
    # Numbers not starting with specified combinations
    "33000000",
    "34300000",
    "35000000",
    "54000000",
    "66600000",  # Number of the beast
    # Numbers with characters other than digits
    "3000A000",
    # Numbers with leading zeroes
    "03000000",
    None,  # if None
]


@pytest.mark.parametrize("number", invalid_numbers)
def test_invalid_phone_numbers(number: str) -> None:
    """Test invalid phone numbers."""
    assert not is_valid_phone_number(number)
