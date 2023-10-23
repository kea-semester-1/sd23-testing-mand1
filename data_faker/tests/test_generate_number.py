import pytest

from data_faker import malthe


@pytest.mark.parametrize(
    "number_value, expected",
    [
        ("42", True),
        ("1", True),
        ("999", True),
        ("42B", True),
        ("1A", True),
        ("999C", True),
        ("0", False),
        ("1000", False),
        ("42BB", False),
        ("42b", False),
        ("42#", False),
    ],
)
def test_validate_number(number_value: str, expected: bool) -> None:
    """Testing if the function works."""
    assert malthe.is_valid_number(number_value) == expected


def test_validate_number_with_none() -> None:
    """Testing if the function raises ValueError for None."""
    with pytest.raises(ValueError, match="Value must be of type string"):
        malthe.is_valid_number(None)  # type: ignore


@pytest.mark.parametrize("number_value", [25, 0, 1, -1, 25.25])
def test_validate_number_with_numeric(number_value: int | float) -> None:
    """Testing if the function raises ValueError for None."""
    with pytest.raises(ValueError, match="Value must be of type string"):
        malthe.is_valid_number(number_value)  # type: ignore
