from fastapi import APIRouter, Query

from data_faker.db import factories
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from typing import Annotated

router = APIRouter()


@router.get("/single")
def create_single() -> FakeInfoDTO:
    """Create fake info."""

    return factories.FakeInfoFactory.create()


@router.get("/batch")
def create_batch(size: Annotated[int, Query(ge=1, le=100)]) -> list[FakeInfoDTO]:
    """Create fake info in batch."""

    return factories.FakeInfoFactory.create_batch(size)
