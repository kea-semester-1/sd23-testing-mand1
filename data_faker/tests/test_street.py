import pytest

from data_faker.db.db_utils import is_valid_street


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
    assert is_valid_street(street_value) == expected
