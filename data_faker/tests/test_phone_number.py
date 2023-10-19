from data_faker.db.mo_utils import is_valid_phone_number
import pytest

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


@pytest.mark.parametrize("prefix", valid_prefixes)
def test_valid_phone_numbers_lower_boundary(prefix: list[str]) -> None:
    """Test a valid phone number for lower boundary partition."""
    number = str(prefix) + "0" * (8 - len(prefix))
    print(number)
    assert is_valid_phone_number(number)


@pytest.mark.parametrize("prefix", valid_prefixes)
def test_valid_phone_numbers_upper_boundary(prefix: str) -> None:
    """Test a valid phone number for upper boundary partition."""
    number = prefix + "9" * (8 - len(prefix))
    print(number)
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
]


@pytest.mark.parametrize("number", invalid_numbers)
def test_invalid_phone_numbers(number: str) -> None:
    """Test invalid phone numbers."""
    assert not is_valid_phone_number(number)
