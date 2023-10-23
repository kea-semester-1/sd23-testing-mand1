from datetime import datetime

import pytest

from data_faker import martin
from data_faker import constants


def test_generate_dob() -> None:
    """Test gen_date."""
    date = martin.generate_random_date_of_birth()
    assert isinstance(date, datetime)
    assert date.year >= constants.MIN_CPR_BIRTH_YEAR
    assert date.year <= constants.MAX_CPR_BIRTH_YEAR


@pytest.mark.parametrize(
    "date",
    [
        datetime(1858, 1, 1),
        datetime(1859, 1, 1),
        datetime(1950, 1, 1),
        datetime(2056, 1, 1),
        datetime(2057, 1, 1),
    ],
)
def test_valid_date_format(date: datetime) -> None:
    """Test validate_date_format."""
    assert martin.validate_date_format(date)


@pytest.mark.parametrize(
    "date",
    [
        datetime(1856, 1, 1),
        datetime(1857, 1, 1),
        datetime(2058, 1, 1),
        datetime(2059, 1, 1),
        None,
        0,
        "",
    ],
)
def test_invalid_date_format(date: datetime) -> None:
    """Test validate_date_format."""
    with pytest.raises(ValueError):
        martin.validate_date_format(date)
