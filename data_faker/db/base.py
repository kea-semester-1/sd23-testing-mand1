from sqlalchemy.orm import DeclarativeBase

from data_faker.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
