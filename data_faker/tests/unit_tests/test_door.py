import pytest
from data_faker.db.utils import is_valid_door_value


@pytest.mark.parametrize(
    "value,expected",
    [
        # Test for predefined floors
        ("th", True),
        ("mf", True),
        ("tv", True),
        ("xy", False),  # Random string
        ("tvf", False),  # Too long predefined string
        ("f", False),  # Too short predefined string
        # Test for numbers from 1 to 50
        ("1", True),
        ("25", True),
        ("0", False),  # test for zero
        ("-1", False),  # test for negative number
        # Boundry partitons
        ("49", True),  # test for upper boundary valid partition
        ("50", True),  # test for highest value possible
        ("51", False),  # test for upper boundary invalid partition
        # Test for lowercase letter optionally followed by a dash
        # and then one to three numeric digits
        ("a1", True),
        ("a-1", True),
        ("z99", True),
        ("z99", True),
        ("z999", True),
        ("z-999", True),
        ("0a", False),  # Number starts with 0
        ("ab1", False),  # Two letters
        ("0a-01", False),  # Leading zeros
        ("a-1000", False),  # Too many digits
        ("a-", False),  # No integers after the dash
        ("Z99", False),  # Uppercase letters
        # Other
        (None, False),  # None value
        ("", False),  # Empty string
        (" ", False),  # Empty string with a space
    ],
)
def test_validate_door_value(value: str, expected: bool) -> None:
    """Test the validate door function."""
    assert is_valid_door_value(value) == expected
