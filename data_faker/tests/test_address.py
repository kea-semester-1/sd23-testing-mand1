import pytest
from data_faker.db.dao.address_dao import AddressDAO
from sqlalchemy.ext.asyncio import AsyncSession
from data_faker.db.models.models import Address
from sqlalchemy.exc import NoResultFound


@pytest.mark.anyio
async def test_get_random_address(dbsession: AsyncSession, address_data: None) -> None:
    """Testing getting a row from the db."""
    address_dao = AddressDAO(dbsession)
    address = await address_dao.get_random_row()

    assert address


@pytest.mark.anyio
async def test_get_random_address_return_model(
    dbsession: AsyncSession, address_data: None
) -> None:
    """Testing getting a row from the db, and check if it returns model."""
    address_dao = AddressDAO(dbsession)
    address = await address_dao.get_random_row()

    assert type(address[0]) == Address


@pytest.mark.anyio
async def test_get_random_address_different_row(
    dbsession: AsyncSession, address_data: None
) -> None:
    """
    Testing getting a row from the db twice, and check if it returns a different choice.
    """
    address_dao = AddressDAO(dbsession)
    address1 = await address_dao.get_random_row()
    address2 = await address_dao.get_random_row()

    assert address1 and address2

    assert address1[0].postal_code != address2[0].postal_code


@pytest.mark.anyio
async def test_get_random_address_no_addresses_loaded(
    dbsession: AsyncSession,
) -> None:
    """
    Testing getting a row from the db, when the table is empty.
    """
    address_dao = AddressDAO(dbsession)

    with pytest.raises(NoResultFound, match="No row found."):
        await address_dao.get_random_row()
