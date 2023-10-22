from datetime import datetime

import pytest

from data_faker import martin
from data_faker.db.enums import Gender
from data_faker import constants


def _create_date(day: int, month: int, year: int) -> datetime:
    """Create date for tests."""
    return datetime(year, month, day)


def _cpr_year_with_seventh(seventh: int, full_year: int) -> tuple[str, str]:
    """Create CPR with seventh cipher."""
    return (f"000000{seventh}000", str(full_year))


@pytest.mark.parametrize(
    "cpr",
    [
        "3112990123",
        "3011980123",
        "0101000123",
        "0202010123",
        "1506550123",
    ],
)
def test_valid_cpr_format(
    cpr: str,
) -> None:
    """Test get_seventh_cipher_range."""

    assert martin.validate_cpr_format(cpr) is True


@pytest.mark.parametrize(
    "cpr",
    [
        "3201200000",
        "0113200000",
        "2902930000",
        "3006x80000",
        "04070100000",
        "281004971",
        "1231040000",
    ],
)
def test_invalid_cpr_format(cpr: str) -> None:
    """Test get_seventh_cipher_range."""
    with pytest.raises(ValueError):
        martin.validate_cpr_format(cpr)


@pytest.mark.parametrize(
    "year, expected_ciphers",
    [
        ("1857", []),
        ("1858", ["5", "6", "7", "8"]),
        ("1899", ["5", "6", "7", "8"]),
        ("1900", ["0", "1", "2", "3"]),
        ("1937", ["0", "1", "2", "3", "4", "9"]),
        ("1999", ["0", "1", "2", "3", "4", "9"]),
        ("2000", ["4", "5", "6", "7", "8", "9"]),
        ("2036", ["4", "5", "6", "7", "8", "9"]),
        ("2057", ["5", "6", "7", "8"]),
        ("2058", []),
    ],
)
def test_generate_seventh_cipher_range(
    year: str,
    expected_ciphers: list[str],
) -> None:
    """Test generate_seventh_cipher_range."""

    assert martin.generate_seventh_cipher_range(year) == expected_ciphers


@pytest.mark.parametrize(
    "cpr, gender",
    [
        ("0000000001", Gender.male),
        ("0000000003", Gender.male),
        ("0000000005", Gender.male),
        ("0000000007", Gender.male),
        ("0000000009", Gender.male),
        ("0000000000", Gender.female),
        ("0000000002", Gender.female),
        ("0000000004", Gender.female),
        ("0000000006", Gender.female),
        ("0000000008", Gender.female),
    ],
)
def test_valid_gender_match(cpr: str, gender: Gender) -> None:
    """Test valid partitions for validate_gender_match."""

    assert martin.validate_gender_match(cpr, gender)


@pytest.mark.parametrize(
    "cpr, gender",
    [
        ("0000000001", Gender.female),
        ("0000000003", Gender.female),
        ("0000000005", Gender.female),
        ("0000000007", Gender.female),
        ("0000000009", Gender.female),
        ("0000000000", Gender.male),
        ("0000000002", Gender.male),
        ("0000000004", Gender.male),
        ("0000000006", Gender.male),
        ("0000000008", Gender.male),
    ],
)
def test_invalid_gender_match(cpr: str, gender: Gender) -> None:
    """Test valid partitions for validate_gender_match."""

    with pytest.raises(ValueError):
        martin.validate_gender_match(cpr, gender)


@pytest.mark.parametrize(
    "cpr, full_year",
    [
        _cpr_year_with_seventh(5, constants.MIN_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(6, constants.MIN_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(7, constants.MIN_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(8, constants.MIN_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(0, 1999),
        _cpr_year_with_seventh(9, 1999),
        _cpr_year_with_seventh(4, 2000),
        _cpr_year_with_seventh(9, 2000),
        _cpr_year_with_seventh(5, constants.MAX_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(6, constants.MAX_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(7, constants.MAX_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(8, constants.MAX_CPR_BIRTH_YEAR),
    ],
)
def test_valid_seventh_cipher(cpr: str, full_year: str) -> None:
    """Test valid partitions for validate_seventh_cipher."""
    assert martin.validate_seventh_cipher(cpr, full_year)


@pytest.mark.parametrize(
    "cpr, full_year",
    [
        _cpr_year_with_seventh(0, constants.MIN_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(4, constants.MIN_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(-1, constants.MIN_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(1, constants.MAX_CPR_BIRTH_YEAR),
        _cpr_year_with_seventh(9, constants.MAX_CPR_BIRTH_YEAR),
    ],
)
def test_invalid_seventh_cipher(cpr: str, full_year: str) -> None:
    """Test valid partitions for validate_seventh_cipher."""

    with pytest.raises(ValueError):
        martin.validate_seventh_cipher(cpr, full_year)


@pytest.mark.parametrize("gender", [Gender.male, Gender.female])
def test_valid_random_last_cipher(gender: Gender) -> None:
    """Test valid partitions for generate_random_last_cipher."""
    last_cipher = martin.generate_random_last_cipher(gender)
    valid_ciphers = (
        constants.MALE_LAST_CIPHERS
        if gender == Gender.male
        else constants.FEMALE_LAST_CIPHERS
    )

    assert last_cipher not in ["-1", "10"]
    assert last_cipher in valid_ciphers


@pytest.mark.parametrize("gender", [Gender.male, Gender.female])
def test_invalid_random_last_cipher(gender: Gender) -> None:
    """Test invalid partitions for generate_random_last_cipher."""
    last_cipher = martin.generate_random_last_cipher(gender)
    invalid_ciphers = (
        constants.FEMALE_LAST_CIPHERS
        if gender == Gender.male
        else constants.MALE_LAST_CIPHERS
    )

    assert last_cipher not in invalid_ciphers


@pytest.mark.parametrize(
    "date_of_birth, gender",
    [
        (_create_date(1, 1, constants.MIN_CPR_BIRTH_YEAR), Gender.female),
        (_create_date(1, 1, constants.MIN_CPR_BIRTH_YEAR + 1), Gender.male),
        (_create_date(1, 1, constants.MAX_CPR_BIRTH_YEAR), Gender.male),
        (_create_date(1, 1, constants.MAX_CPR_BIRTH_YEAR - 1), Gender.female),
    ],
)
def test_valid_generate_cpr(date_of_birth: datetime, gender: Gender) -> None:
    """Test valid partitions for generate_cpr."""

    cpr = martin.generate_cpr(date_of_birth, gender)
    cpr = cpr.replace("-", "")

    assert martin.validate_gender_match(cpr, gender)
    assert martin.validate_cpr_format(cpr)
    assert martin.validate_seventh_cipher(cpr, str(date_of_birth.year))


@pytest.mark.parametrize(
    "date_of_birth, gender",
    [
        (_create_date(1, 1, constants.MIN_CPR_BIRTH_YEAR - 1), Gender.female),
        (_create_date(1, 1, constants.MIN_CPR_BIRTH_YEAR - 2), Gender.male),
        (_create_date(1, 1, constants.MAX_CPR_BIRTH_YEAR + 1), Gender.male),
        (_create_date(1, 1, constants.MAX_CPR_BIRTH_YEAR + 2), Gender.female),
    ],
)
def test_invalid_generate_cpr(date_of_birth: datetime, gender: Gender) -> None:
    """Test valid partitions for generate_cpr."""

    with pytest.raises(ValueError):
        martin.generate_cpr(date_of_birth, gender)
