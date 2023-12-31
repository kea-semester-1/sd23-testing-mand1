import pytest

from data_faker.db import utils


@pytest.mark.parametrize(
    "street_value, expected",
    [
        ("Nørrebrogade", True),
        ("Elmegade", True),
        ("Sønder Fasanvej", True),
        ("Henrik Nielsens Vej", True),
        ("王府井大街", False),  # Chinese
        ("רחוב הכוכב", False),  # Hebrew
        ("Elmegade 4", False),
        ("", False),
        ("Hans Petersens Vej#", False),
        ("#Hans Hansens Gade", False),
        ("Latin Str€€t", False),
    ],
)
def test_validate_street(street_value: str, expected: bool) -> None:
    """Testing if the function works."""
    assert utils.is_valid_street(street_value) == expected


def test_validate_street_with_none() -> None:
    """Testing if the function raises ValueError for None."""
    with pytest.raises(ValueError, match="Value must be of type string"):
        utils.is_valid_street(None)  # type: ignore


@pytest.mark.parametrize("name", [25, 0, 25.25, -25])
def test_validate_name_with_numeric(name: int | float) -> None:
    """Testing if the function raises errors with numeric values outside of string."""
    with pytest.raises(ValueError, match="Value must be of type string"):
        utils.is_valid_street(name)  # type: ignore
