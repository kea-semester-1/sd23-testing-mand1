import pytest

from data_faker.malthe import extract_person_info
from data_faker.db.db_utils import is_valid_name
from data_faker.web.dtos.person_info_dto import PersonInfoDTO


@pytest.mark.parametrize(
    "person_info",
    extract_person_info("input_files/person-names.json"),
)
def test_is_valid_name(person_info: PersonInfoDTO) -> None:
    """Testing if the function works."""

    assert is_valid_name(person_info.name)
    assert is_valid_name(person_info.surname)


def test_is_valid_name_wrong_path() -> None:
    """Testing if the function works."""

    with pytest.raises(FileNotFoundError):
        extract_person_info("input_files/persons.json")  # File does not exist


invalid_names = [
    "Casper1",  # including a numeric value
    "Ca#sper!",  # including special characters, not being an alphabetic difference
    "",  # empty string
    " Casper",  # starting with a space
    "123512123",  # only numeric values
    "珀ØΚάσ",  # Mixing language characters. Danish, Chinese & Greek
    "カスパー",  # Japanese
    "Malthe ",  # Trailing space
]


@pytest.mark.parametrize("name", invalid_names)
def test_invalid_names(name: str) -> None:
    """Testing if the function works."""
    assert not is_valid_name(name), f"Failed for name: {name}"
