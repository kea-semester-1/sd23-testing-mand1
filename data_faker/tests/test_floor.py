import pytest

from data_faker import malthe


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
def test_validate_floor(floor_value: str, expected: bool) -> None:
    """Testing if the function works."""
    assert malthe.is_valid_floor(floor_value) == expected


def test_validate_floor_with_none() -> None:
    """Testing if the function raises ValueError for None."""
    with pytest.raises(ValueError, match="Value must be of type string"):
        malthe.is_valid_number(None)
