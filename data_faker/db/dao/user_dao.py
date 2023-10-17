from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data_faker.db.dependencies import get_db_session
from data_faker.db.models.models import User, Address
import sqlalchemy as sa
from data_faker.db.factories import UserFactory, AddressFactory


class UserDAO:
    """UserDAO."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self) -> None:  # TODO: Return id
        """Create function for User DAO."""
        address = AddressFactory()
        user = UserFactory()

        self.session.add(address)
        await self.session.commit()

        self.session.add(user)
        await self.session.commit()

    async def get_all(self) -> list[User]:
        """Retrieve all users."""

        query = sa.select(User)

        users = await self.session.execute(query)

        return list(users.scalars().fetchall())

    async def get_all_with_address(self) -> list[dict]:
        """Get all users with their addresses."""

        query = sa.select(User, Address).join(Address, User.address_id == Address.id)
        result = await self.session.execute(query)
        rows = result.fetchall()

        combined = []
        for user, address in rows:
            user_data = {
                "id": user.id,
                "gender": user.gender,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "cpr": user.cpr,
                "date_of_birth": str(user.date_of_birth),
                "phone_number": user.phone_number,
                "address_id": str(user.address_id),
                "address": {
                    "street": address.street,
                    "number": address.number,
                    "floor": address.floor,
                    "town": address.town,
                    "postal_code": address.postal_code,
                },
            }
            combined.append(user_data)

        return combined
