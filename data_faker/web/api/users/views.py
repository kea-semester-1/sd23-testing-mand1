from fastapi import APIRouter, Depends, Query
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from data_faker.db.factories import FakeInfoFactory
from data_faker.db import mo_utils as utils
from data_faker.db.dao.address_dao import AddressDAO

router = APIRouter()


@router.get("/factory-demo")
async def factory_demo(
    address_dao: AddressDAO = Depends(utils.get_address_dao),
    limit: int = 1,
) -> list[FakeInfoDTO]:
    """Create fake info batch demo."""
    addresses = await address_dao.get_random_row(limit=limit)
    return FakeInfoFactory.create_batch(limit, addresses=addresses)
