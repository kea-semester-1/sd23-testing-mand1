import pytest

from data_faker.db.utils import is_valid_floor


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
