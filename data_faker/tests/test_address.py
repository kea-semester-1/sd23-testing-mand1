import pytest
from data_faker.db.dao.address_dao import AddressDAO
from sqlalchemy.ext.asyncio import AsyncSession



@pytest.mark.anyio
async def test_get_address(dbsession: AsyncSession) -> None:
    address = AddressDAO(dbsession)

    await address.create()
    address_1 = await address.get_random_row()

    print(address_1)
