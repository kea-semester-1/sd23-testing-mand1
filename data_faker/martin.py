import random
from datetime import datetime

from data_faker.db.enums import Gender

MIN_BIRTH_YEAR = 1858
MAX_BIRTH_YEAR = 2057

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
    """Validate if the gender matches the CPR number."""
    last_cipher_is_even = int(cpr[-1]) % 2 == 0

    if last_cipher_is_even and str(gender) == str(Gender.male):
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

    print(gender, Gender.male, gender == Gender.male)
    return (
        str(random.choice([1, 3, 5, 7, 9]))
        if gender == Gender.male
        else str(random.choice([0, 2, 4, 6, 8]))
    )


def get_validated_cpr(cpr: str, year: str, gender: Gender) -> str:
    """Validate and return cpr."""

    cpr_stripped = cpr.replace("-", "")

    validate_cpr_format(cpr_stripped)
    validate_gender_match(cpr_stripped, gender)
    validate_seventh_cipher(cpr_stripped, year)

    return cpr


def generate_cpr(date_of_birth: datetime, gender: Gender) -> str:
    """Generate a CPR number based on date of birth and gender."""

    if date_of_birth.year < MIN_BIRTH_YEAR:
        raise ValueError(
            f"Cannot generate CPR-Number for birth years less than {MIN_BIRTH_YEAR}"
        )

    if date_of_birth.year > MAX_BIRTH_YEAR:
        raise ValueError(
            f"Cannot  generate CPR-Number for birth years greater than {MAX_BIRTH_YEAR}"
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
    cpr = f"{dob_ciphers}-{control_ciphers}"

    return get_validated_cpr(cpr, year, gender)
