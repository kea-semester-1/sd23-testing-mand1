from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data_faker.db.dependencies import get_db_session
from data_faker.db.models.models import User
import sqlalchemy as sa
from data_faker.db.factories import UserFactory, AddressFactory


class UserDAO:
    """UserDAO."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self) -> None:  # TODO: Return id
        """Create function for User DAO."""
        address = AddressFactory()
        # address = Address(
        #     street="Gade",
        #     number="26",
        #     floor="5",
        #     door="3",
        #     town="København",
        #     postal_code=2,
        # )

        user = UserFactory()
        # user = User(
        #     first_name="Malthe",
        #     last_name="Gram",
        #     gender="male",
        #     cpr="22222222",
        #     date_of_birth=datetime.now(),
        #     address=address,
        #     phone_number="22222",
        # )

        self.session.add(address)
        await self.session.commit()

        self.session.add(user)
        await self.session.commit()

    async def get_all(self) -> list[User]:
        """Retrieve all users."""

        query = sa.select(User)

        users = await self.session.execute(query)

        return list(users.scalars().fetchall())
