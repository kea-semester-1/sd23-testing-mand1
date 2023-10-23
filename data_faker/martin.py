import random
from datetime import datetime, timedelta
from data_faker import constants

from data_faker.db.enums import Gender

SEVENTH_CIPHER_MAPPING = {
    0: [(1900, 1999)],
    1: [(1900, 1999)],
    2: [(1900, 1999)],
    3: [(1900, 1999)],
    4: [(1937, 1999), (2000, 2036)],
    5: [(1858, 1899), (2000, 2057)],
    6: [(1858, 1899), (2000, 2057)],
    7: [(1858, 1899), (2000, 2057)],
    8: [(1858, 1899), (2000, 2057)],
    9: [(1937, 1999), (2000, 2036)],
}


def generate_seventh_cipher_range(year: str) -> list[str]:
    """Get a range of valid seventh ciphers, based on the year of birth."""
    return [
        str(key)
        for key, value in SEVENTH_CIPHER_MAPPING.items()
        if any(min_val <= int(year) <= max_val for min_val, max_val in value)
    ]


def validate_cpr_format(cpr: str) -> bool:
    """Validate the format of a CPR number."""

    invalid_input = cpr is None or not isinstance(cpr, str)

    if invalid_input:
        raise ValueError("Invalid input.")

    if len(cpr) != 10:
        raise ValueError(f"Invalid CPR number length. Length: {len(cpr)} ")

    if not cpr.isdigit():
        raise ValueError("Non-digit characters in CPR number.")

    dob = cpr[:6]
    date_format = "%d%m%y"

    try:
        datetime.strptime(dob, date_format)
    except ValueError as e:
        raise e

    return True


def validate_gender_match(cpr: str, gender: Gender) -> bool:
    """
    Validate if the gender matches the CPR number.

    If male: last cipher is odd
    If female: last cipher is even
    """

    if gender is None or cpr is None:
        raise ValueError("Invalid input.")

    if len(cpr) != 10:
        raise ValueError(f"Invalid CPR number length. Length: {len(cpr)} ")

    last_cipher_is_even = int(cpr[-1]) % 2 == 0

    gender_mismatch = (
        last_cipher_is_even
        and gender == Gender.male
        or not last_cipher_is_even
        and gender == Gender.female
    )

    if gender_mismatch:
        raise ValueError(f"Gender mismatch. gender: {gender}, last cipher: {cpr[-1]}")

    return True


def validate_seventh_cipher(cpr: str, full_year: str) -> bool:
    """Validate the seventh cipher of a CPR number."""
    seventh_cipher = cpr[6]
    valid_range = generate_seventh_cipher_range(full_year)

    if seventh_cipher not in valid_range:
        raise ValueError(
            f"Invalid seventh cipher. Cipher: {seventh_cipher},"
            f"year: {full_year}, range: {valid_range}",
        )

    return True


def generate_random_last_cipher(gender: Gender) -> str:
    """Generate the last cipher, based on gender."""

    return (
        str(random.choice([1, 3, 5, 7, 9]))
        if gender == Gender.male
        else str(random.choice([0, 2, 4, 6, 8]))
    )


def generate_cpr(date_of_birth: datetime, gender: Gender) -> str:
    """Generate a CPR number based on date of birth and gender."""

    invalid_input = (
        date_of_birth is None
        or gender is None
        or not isinstance(date_of_birth, datetime)
        or not isinstance(gender, Gender)
    )

    if invalid_input:
        raise ValueError("Invalid input.")

    invalid_date_range = (
        date_of_birth.year < constants.MIN_CPR_BIRTH_YEAR
        or date_of_birth.year > constants.MAX_CPR_BIRTH_YEAR
    )

    if invalid_date_range:
        raise ValueError(
            f"Cannot generate CPR-Number for birth years"
            f" less than {constants.MIN_CPR_BIRTH_YEAR}"
            f" or greater than {constants.MAX_CPR_BIRTH_YEAR}",
        )

    day = f"{date_of_birth.day:02}"
    month = f"{date_of_birth.month:02}"
    year = str(date_of_birth.year)
    year_short = year[-2:]

    seventh_cipher = random.choice(generate_seventh_cipher_range(year))
    eighth_cipher = random.randrange(0, 9)
    ninth_cipher = random.randrange(0, 9)
    last_cipher = generate_random_last_cipher(gender)

    dob_ciphers = f"{day}{month}{year_short}"
    control_ciphers = f"{seventh_cipher}{eighth_cipher}{ninth_cipher}{last_cipher}"
    return f"{dob_ciphers}-{control_ciphers}"


#######
# DOB #
#######


def generate_random_date_of_birth() -> datetime:
    """Generate a random date of birth."""
    start_date = datetime(constants.MIN_CPR_BIRTH_YEAR, 1, 1)
    end_date = datetime(constants.MAX_CPR_BIRTH_YEAR, 12, 31)
    days_between_dates = (end_date - start_date).days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)


def validate_date_format(date: datetime) -> bool:
    """Validate a date of birth."""

    if date is None or not isinstance(date, datetime):
        raise ValueError("Invalid input.")

    invalid_date_range = (
        date.year < constants.MIN_CPR_BIRTH_YEAR
        or date.year > constants.MAX_CPR_BIRTH_YEAR
    )

    if invalid_date_range:
        raise ValueError("Invalid date range.")

    return True
