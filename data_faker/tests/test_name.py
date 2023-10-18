import pytest

from data_faker.db.factories import extract_person_info
from data_faker.db.utils_malthe import is_valid_name


def test_is_valid_name():
    for _ in range(100):
        person_info = extract_person_info()

        assert is_valid_name(person_info['first_name'])
        assert is_valid_name(person_info['last_name'])



invalid_names = [
    "Casper1",      # including a numeric value
    "Ca#sper!",     # including special characters, not being an alphabetic difference
    "",             # empty string
    " Casper",      # starting with a space
    "123512123",    # only numeric values
    "珀ØΚάσ"        # Mixing language characters. Danish, Chinese & Greek
]

@pytest.mark.parametrize("name", invalid_names)
def test_invalid_names(name):
    assert not is_valid_name(name), f"Failed for name: {name}"
