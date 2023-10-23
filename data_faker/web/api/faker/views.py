from fastapi import APIRouter, Query, Depends

from data_faker.db import factories
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from typing import Annotated
from data_faker.db import mo_utils as utils
from data_faker.db.dao.address_dao import AddressDAO

router = APIRouter()


@router.get("/single")
async def create_single(
    address_dao: AddressDAO = Depends(utils.get_address_dao),
) -> FakeInfoDTO:
    """Create fake info."""
    address = await address_dao.get_random_row()
    return factories.FakeInfoFactory.create(address_info=address[0])


@router.get("/batch")
async def create_batch(
    size: Annotated[int, Query(ge=1, le=100)],
    address_dao: AddressDAO = Depends(utils.get_address_dao),
) -> list[FakeInfoDTO]:
    """Create fake info in batch."""
    addresses = await address_dao.get_random_row(limit=size)
    return factories.FakeInfoFactory.create_batch(size, address_info=addresses)
