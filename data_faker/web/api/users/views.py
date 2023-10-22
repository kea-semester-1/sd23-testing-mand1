from fastapi import APIRouter, Depends
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from data_faker.db.factories import FakeInfoFactory
from data_faker.db import mo_utils as utils

router = APIRouter()


@router.get("/factory-demo")
async def factory_demo(
    address_dao=Depends(utils.get_address_dao),
) -> list[FakeInfoDTO]:
    """Create fake info batch demo."""
    addresses = await utils.get_random_postal_code_and_town(
        address_dao=address_dao, limit=10
    )
    for address in addresses:
        print(address.__dict__)
    return FakeInfoFactory.create_batch(10, addresses=addresses)
