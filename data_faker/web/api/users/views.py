from fastapi import APIRouter
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from data_faker.db.factories import FakeInfoFactory

router = APIRouter()


@router.get("/factory-demo")
def factory_demo() -> list[FakeInfoDTO]:
    """Create fake info batch demo."""

    return FakeInfoFactory.create_batch(10)
