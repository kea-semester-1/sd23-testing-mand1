from fastapi import APIRouter, Query

from data_faker.db import factories
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO, EmbedDTO
from typing import Annotated
from fastapi import Depends

router = APIRouter()


@router.get(
    "/single",
    response_model_exclude_none=True,
)
def get_single(
    embed: Annotated[EmbedDTO, Depends()],
) -> FakeInfoDTO:
    """Get fake info."""

    fake_info = factories.FakeInfoFactory.create()
    address = fake_info.address

    embed_dict = embed.model_dump(exclude_none=True)

    person_dict = {
        key: getattr(fake_info, key)
        for key, value in embed_dict.items()
        if hasattr(fake_info, key) and value is True
    }

    address_dict = {
        key: getattr(address, key)
        for key, value in embed_dict.items()
        if hasattr(address, key) and value is True
    }

    fake_info_dict = {**person_dict}

    if address_dict:
        fake_info_dict["address"] = {**address_dict}

    return FakeInfoDTO(**fake_info_dict)


@router.get(
    "/batch",
    response_model_exclude_none=True,
)
def get_batch(
    embed: Annotated[EmbedDTO, Depends()],
    size: Annotated[int, Query(ge=1, le=100)] = 1,
) -> list[FakeInfoDTO]:
    """Get a batch of fake info."""

    fake_infos = factories.FakeInfoFactory.create_batch(size)

    embed_dict = embed.model_dump(exclude_none=True)
    fake_info_dicts: list[FakeInfoDTO] = []

    for fake_info in fake_infos:
        address = fake_info.address

        person_dict = {
            key: getattr(fake_info, key)
            for key, value in embed_dict.items()
            if hasattr(fake_info, key) and value is True
        }

        address_dict = {
            key: getattr(address, key)
            for key, value in embed_dict.items()
            if hasattr(address, key) and value is True
        }

        fake_info_dict = {**person_dict}

        if address_dict:
            fake_info_dict["address"] = {**address_dict}

        fake_info_dicts.append(FakeInfoDTO(**fake_info_dict))

    return fake_info_dicts


@router.get("/demo-single")
def get_demo_single() -> FakeInfoDTO:
    """Demo for fake info."""
    return factories.FakeInfoFactory.create()


@router.get("/demo-batch")
def get_demo_batch(
    size: Annotated[int, Query(ge=1, le=100)] = 1,
) -> list[FakeInfoDTO]:
    """Demo for a batch of fake info."""
    return factories.FakeInfoFactory.create_batch(size)
