import pytest
from data_faker.db.mo_utils import (
    validate_door_value,
)  # Adjust the import according to your module setup.


@pytest.mark.parametrize(
    "value,expected",
    [
        # Test for predefined strings
        ("th", True),
        ("mf", True),
        ("tv", True),
        ("abc", False),  # Random string
        ("tvf", False),  # Too long predefined string
        # Test for numbers from 1 to 50
        ("1", True),
        ("25", True),
        ("50", True),
        ("51", False),
        ("0", False),
        ("-1", False),
        # Test for lowercase letter optionally followed by a dash and then one to three numeric digits
        ("a1", True),
        ("a-1", True),
        ("z999", True),
        ("z-999", True),
        ("0a", False),  # Number starts with 0
        ("ab1", False),  # Two letters
        ("0a-01", False),  # Leading zeros
        ("a-1000", False),  # Too many digits
    ],
)
def test_validate_door_value(value, expected):
    assert validate_door_value(value) == expected
