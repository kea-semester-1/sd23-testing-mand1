import pytest
from data_faker.db.utils_malthe import is_valid_number


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
def test_validate_number(number_value, expected):
    assert is_valid_number(number_value) == expected
