from fastapi import APIRouter, Depends
from data_faker.db.dao.user_dao import UserDAO

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
