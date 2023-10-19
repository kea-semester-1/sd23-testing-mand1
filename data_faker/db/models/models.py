import uuid
from datetime import datetime
from typing import Any
from collections.abc import Callable

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from data_faker.db.meta import meta


class Base(DeclarativeBase):
    """Base setup for all models including UUID."""

    metadata = meta

    __tablename__: str
    __init__: Callable[..., Any]
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )


class Address(Base):
    """Address model."""

    __tablename__ = "address"

    town: Mapped[str] = mapped_column(sa.String(255))
    postal_code: Mapped[int] = mapped_column(sa.Integer)


class User(Base):
    """User model."""

    __tablename__ = "user"

    first_name: Mapped[str] = mapped_column(sa.String(255))
    last_name: Mapped[str] = mapped_column(sa.String(255))
    gender: Mapped[str] = mapped_column(sa.String(255))
    cpr: Mapped[str] = mapped_column(sa.String(255))
    date_of_birth: Mapped[datetime] = mapped_column(sa.Date)
    phone_number: Mapped[str] = mapped_column(sa.String(255))
