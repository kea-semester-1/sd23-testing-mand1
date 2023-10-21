import pytest

from data_faker import martin

# TODO: Add more parametrized tests (Black box testing)


@pytest.mark.parametrize(
    "year, expected",
    [("1997", ["0", "1", "2", "3", "4", "9"])],
)
def test_get_seventh_cipher_range(year: str, expected: list[str]) -> None:
    """Test get_seventh_cipher_range."""
    actual = martin.generate_seventh_cipher_range(year)
    assert actual == expected


@pytest.mark.parametrize(
    "cpr, full_year",
    [("0404975069", "1997")],
)
def test_validate_seventh_cipher(
    cpr: str,
    full_year: str,
) -> None:
    """Test get_seventh_cipher_range."""
    with pytest.raises(ValueError):
        martin.validate_seventh_cipher(cpr, full_year)


@pytest.mark.parametrize(
    "cpr",
    ["12345678900", "i234567890", "4040971069"],
)
def test_validate_cpr_format(
    cpr: str,
) -> None:
    """Test get_seventh_cipher_range."""
    with pytest.raises(ValueError):
        martin.validate_cpr_format(cpr)


# TODO: Test generate_last_cipher + validate_gender_match

# TODO: Test generate_cpr

# TODO: Look up partitioning and equivalence classes etc
