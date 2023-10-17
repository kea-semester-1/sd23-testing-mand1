from datetime import datetime
from data_faker.db.enums import Gender
import random

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


def get_seventh_cipher_range(year: str) -> list[str]:
    """Get a range of valid seventh ciphers, based on the year of birth."""
    return [
        str(key)
        for key, value in SEVENTH_CIPHER_MAPPING.items()
        if any(min_val <= int(year) <= max_val for min_val, max_val in value)
    ]


def validate_cpr_format(cpr: str) -> None:
    """Validate the format of a CPR number."""
    if len(cpr) != 10:
        raise ValueError(f"Invalid CPR number length. Length: {len(cpr)} ")

    if not cpr.isdigit():
        raise ValueError("Non-digit characters in CPR number.")

    dob = cpr[:6]
    day, month, year = map(int, [dob[:2], dob[2:4], dob[4:]])

    if not (1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 99):
        raise ValueError("Invalid date of birth.")


def validate_gender_match(cpr: str, gender: Gender) -> None:
    """Validate if the gender matches the CPR number."""
    last_cipher_is_even = int(cpr[-1]) % 2 == 0

    if last_cipher_is_even and gender == Gender.male:
        raise ValueError(f"Gender mismatch. gender: {gender}, last cipher: {cpr[-1]}")


def validate_seventh_cipher(cpr: str, full_year: str) -> None:
    """Validate the seventh cipher of a CPR number."""
    seventh_cipher = cpr[6]
    valid_range = get_seventh_cipher_range(full_year)

    if seventh_cipher not in valid_range:
        raise ValueError(
            f"Invalid seventh cipher. Cipher: {seventh_cipher},"
            f"year: {full_year}, range: {valid_range}"
        )


def generate_random_last_cipher(gender: Gender) -> str:
    """Generate the last cipher, based on gender."""
    return (
        str(random.choice([1, 3, 5, 7, 9]))
        if gender == Gender.male
        else str(random.choice([0, 2, 4, 6, 8]))
    )


def generate_cpr(date_of_birth: datetime, gender: Gender) -> str:
    """Generate a CPR number based on date of birth and gender."""
    day = f"{date_of_birth.day:02}"
    month = f"{date_of_birth.month:02}"
    year = str(date_of_birth.year)
    year_short = year[-2:]

    seventh_cipher = random.choice(get_seventh_cipher_range(year))
    eighth_cipher = random.randrange(0, 9)
    ninth_cipher = random.randrange(0, 9)
    last_cipher = generate_random_last_cipher(gender)

    dob_ciphers = f"{day}{month}{year_short}"
    control_ciphers = f"{seventh_cipher}{eighth_cipher}{ninth_cipher}{last_cipher}"
    cpr = f"{dob_ciphers}-{control_ciphers}"
    cpr_stripped = cpr.replace("-", "")

    validate_cpr_format(cpr_stripped)
    validate_gender_match(cpr_stripped, gender)
    validate_seventh_cipher(cpr_stripped, year)

    return cpr
