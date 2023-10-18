from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data_faker.db.dependencies import get_db_session
from data_faker.db.models.models import Address
import sqlalchemy as sa


class AddressDAO:
    """AddressDAO."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self) -> None:  # TODO: Return id
        """Create function for address DAO."""

        address = Address(town="Frederiksberg", postal_code=2000)

        self.session.add(address)
        await self.session.commit()

    async def get_random_row(self) -> Address:
        """Retrieve random row from address table."""

        # Assuming you're using SQLite; use func.rand() for MySQL, etc.
        query = sa.select(Address).order_by(sa.func.random()).limit(1)

        result = await self.session.execute(query)
        address = result.scalars().first()

        # It's better to use logging instead of print for such cases, but let's keep it for now
        print(address.town)
        print(address.postal_code)

        return address
