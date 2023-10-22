from fastapi import APIRouter

from data_faker.db import factories
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from data_faker.web.dtos.person_info_dto import PersonInfoDTO

router = APIRouter()


@router.get("/factory-demo")
def factory_demo() -> FakeInfoDTO:
    """Create fake info batch demo."""

    return factories.FakeInfoFactory.create()


@router.get("/factory-demo2")
def test_demo() -> list[PersonInfoDTO]:
    """Create fake info batch demo."""

    return factories.extract_person_info("input_files/person-names.json")
