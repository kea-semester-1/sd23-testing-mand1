import pytest

from data_faker import malthe
from data_faker.malthe import is_valid_name
from data_faker.web.dtos.person_info_dto import PersonInfoDTO


@pytest.mark.parametrize(
    "person_info",
    malthe.extract_person_info("input_files/person-names.json"),
)
def test_is_valid_name(person_info: PersonInfoDTO) -> None:
    """Testing if the function works."""

    assert malthe.is_valid_name(person_info.name)
    assert malthe.is_valid_name(person_info.surname)


def test_is_valid_name_wrong_path() -> None:
    """Testing if the function works."""

    with pytest.raises(FileNotFoundError):
        malthe.extract_person_info("input_files/persons.json")  # File does not exist


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
    assert not malthe.is_valid_name(name), f"Failed for name: {name}"


def test_validate_name_with_none() -> None:
    """Testing if the function raises ValueError for None."""
    with pytest.raises(ValueError, match="Value must be of type string"):
        malthe.is_valid_name(None)  # type: ignore


@pytest.mark.parametrize("name", [25, 0, 25.25, -1, -999])
def test_validate_name_with_numeric(name: int | float) -> None:
    """Testing if the function raises errors with numeric values outside of string."""
    with pytest.raises(ValueError, match="Value must be of type string"):
        is_valid_name(name)  # type: ignore
