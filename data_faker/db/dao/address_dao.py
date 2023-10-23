from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data_faker.db.dependencies import get_db_session
from data_faker.db.models.models import Address
import sqlalchemy as sa
from sqlalchemy.exc import NoResultFound


class AddressDAO:
    """AddressDAO."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def get_random_row(self, limit: int = 1) -> list[Address]:
        """Retrieve random row from address table."""

        query = sa.select(Address).order_by(sa.func.random()).limit(limit=limit)

        result = await self.session.execute(query)
        addresses = result.scalars().fetchall()

        if not addresses:
            raise NoResultFound("No row found.")

        return list(addresses)
