
import pytest

from data_faker.db.utils_malthe import is_valid_floor


# def test_valid_floor() -> None:
#   """Test if generate_floor() produces valid floor values."""
#
#  generated_floor = generate_floor()

# assert generated_floor in range(1,99) or generated_floor == "st"


@pytest.mark.parametrize(
    "floor_value, expected",
    [
        ("st", True),
        ("12", True),
        ("1", True),
        ("99", True),
        ("0", False),
        ("100", False),
        ("1st", False),
        ("sf", False),
        ("2nd", False),
    ],
)
def test_validate_floor(floor_value, expected):
    assert is_valid_floor(floor_value) == expected
