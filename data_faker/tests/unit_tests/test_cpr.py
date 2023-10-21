import pytest

from data_faker import martin
from data_faker.db.factories import FakeInfoFactory
from datetime import datetime
from data_faker.db.enums import Gender

factory = FakeInfoFactory()


def _create_date(day: int, month: int, year: int) -> datetime:
    """Create date for tests."""

    return datetime(year, month, day)


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


# @pytest.mark.parametrize(
#     "cpr, full_year",
#     [
#         ("000000571001", "1857"),
#     ],
# )
# def test_validate_seventh_cipher(
#     cpr: str,
#     full_year: str,
# ) -> None:
#     """Test get_seventh_cipher_range."""
#     with pytest.raises(ValueError):
#         martin.validate_seventh_cipher(cpr, full_year)


@pytest.mark.parametrize(
    "date_of_birth, gender",
    [
        (_create_date(30, 1, 1998), Gender.female),
        (_create_date(31, 12, 1899), Gender.male),
        (_create_date(1, 1, 2001), Gender.male),
        (_create_date(29, 2, 1992), Gender.female),
    ],
)
def test_valid_generate_cpr(date_of_birth: datetime, gender: Gender) -> None:
    """Test valid partitions for generate_cpr."""

    cpr = martin.generate_cpr(date_of_birth, gender)
    cpr = cpr.replace("-", "")

    assert martin.validate_gender_match(cpr, gender)
    assert martin.validate_cpr_format(cpr)
    assert martin.validate_seventh_cipher(cpr, str(date_of_birth.year))


# TODO: Test generate_last_cipher + validate_gender_match

# TODO: Test generate_cpr

# TODO: Look up partitioning and equivalence classes etc
