from fastapi import APIRouter, Depends
from data_faker.db.dao.user_dao import UserDAO
from data_faker.db.models.models import User
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


class UserDTO(BaseModel):
    first_name: str
    last_name: str
    gender: str
    cpr: str
    date_of_birth: datetime
    phone_number: str
    address: str


@router.get("")
async def get_users(dao: UserDAO = Depends()) -> list[UserDTO]:
    """Get all users."""
    users = await dao.get_all()
    return [UserDTO.model_validate(user) for user in users]


@router.post("")
async def create(
    dao: UserDAO = Depends(),
) -> None:
    """Create a new user."""

    return await dao.create()
