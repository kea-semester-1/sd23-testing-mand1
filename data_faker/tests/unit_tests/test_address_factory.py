import pytest

from data_faker.db.factories import AddressFactory
from data_faker.web.dtos.address_dto import AddressDTO
from sqlalchemy.ext.asyncio import AsyncSession

from data_faker.db.dao.address_dao import AddressDAO


@pytest.mark.parametrize(
    "attribute", ["street", "number", "door", "floor", "town", "postal_code"]
)
@pytest.mark.anyio
async def test_address_factory_attribute(
    attribute: str, dbsession: AsyncSession, address_data: None
) -> None:
    """Test each attribute of the address_factory."""
    address_dao = AddressDAO(dbsession)
    address = await address_dao.get_random_row()

    full_address = AddressFactory.create(address=address[0])
    print(address[0].postal_code)
    print(full_address.__dict__)
    assert isinstance(full_address, AddressDTO)

    if attribute == "postal_code":
        value = getattr(full_address, attribute)
        assert isinstance(value, int)
        assert value > 0
        return

    value = getattr(full_address, attribute)
    assert isinstance(value, str)
    assert len(value) > 0
