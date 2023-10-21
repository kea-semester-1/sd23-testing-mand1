from fastapi import APIRouter, Depends
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from data_faker.db.factories import FakeInfoFactory
from data_faker.db import mo_utils as utils

router = APIRouter()


@router.get("/factory-demo")
async def factory_demo(
    address=Depends(utils.get_random_postal_code_and_town),
) -> list[FakeInfoDTO]:
    """Create fake info batch demo."""
    print(address.__dict__)
    return FakeInfoFactory.create_batch(10)
