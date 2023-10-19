from fastapi import APIRouter, Depends
from data_faker.db.dao.user_dao import UserDAO
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from data_faker.db.factories import FakeInfoFactory

router = APIRouter()


@router.get("")
async def get_users(dao: UserDAO = Depends()):
    """Get all users."""
    return await dao.get_all()


@router.post("")
async def create(
    dao: UserDAO = Depends(),
) -> None:
    """Create a new user."""

    return await dao.create()


@router.get("/factory-demo")
def factory_demo() -> list[FakeInfoDTO]:
    """Create fake info batch demo."""

    return FakeInfoFactory.create_batch(10)
