import re
import string

from sqlalchemy import text
from sqlalchemy.engine import make_url
from sqlalchemy.ext.asyncio import create_async_engine

from data_faker.settings import settings


async def create_database() -> None:
    """Create a database."""
    db_url = make_url(str(settings.db_url.with_path("/postgres")))
    engine = create_async_engine(db_url, isolation_level="AUTOCOMMIT")

    async with engine.connect() as conn:
        database_existance = await conn.execute(
            text(
                f"SELECT 1 FROM pg_database WHERE datname='{settings.db_base}'",  # noqa: E501, S608
            ),
        )
        database_exists = database_existance.scalar() == 1

    if database_exists:
        await drop_database()

    async with engine.connect() as conn:  # noqa: WPS440
        await conn.execute(
            text(
                f'CREATE DATABASE "{settings.db_base}" ENCODING "utf8" TEMPLATE template1',  # noqa: E501
            ),
        )


async def drop_database() -> None:
    """Drop current database."""
    db_url = make_url(str(settings.db_url.with_path("/postgres")))
    engine = create_async_engine(db_url, isolation_level="AUTOCOMMIT")
    async with engine.connect() as conn:
        disc_users = (
            "SELECT pg_terminate_backend(pg_stat_activity.pid) "  # noqa: S608
            "FROM pg_stat_activity "
            f"WHERE pg_stat_activity.datname = '{settings.db_base}' "
            "AND pid <> pg_backend_pid();"
        )
        await conn.execute(text(disc_users))
        await conn.execute(text(f'DROP DATABASE "{settings.db_base}"'))

def is_valid_name(name: str) -> bool:
    """
    Validates if the given name contains only English and Danish letters.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    # Regular expression pattern to match only English and Danish letters and spaces, but not starting or ending spaces.
    pattern = r"^[A-Za-zæøåÆØÅ\.][A-Za-zæøåÆØÅ\. ]*[A-Za-zæøåÆØÅ\.]$"

    return bool(re.match(pattern, name))


def is_valid_floor(s: str) -> bool:
    if s == "st":
        return True
    if s.isdigit() and 1 <= int(s) <= 99:
        return True
    return False


def is_valid_number(s: str) -> bool:
    if s.isdigit() and 1 <= int(s) <= 999:
        return True
    if s[-1] in string.ascii_uppercase and s[:-1].isdigit() and 1 <= int(s[:-1]) <= 999:
        return True
    return False

def is_valid_street(name: str) -> bool:
    pattern = r"^[A-Za-zæøåÆØÅ\.][A-Za-zæøåÆØÅ\. ]*[A-Za-zæøåÆØÅ\.]$"

    return bool(re.match(pattern, name))
