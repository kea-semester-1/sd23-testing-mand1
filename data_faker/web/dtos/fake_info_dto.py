from pydantic import BaseModel
from datetime import datetime
from data_faker.db.enums import Gender
from data_faker.web.dtos.address_dto import AddressDTO


class FakeInfoDTO(BaseModel):
    """Fake Info DTO."""

    gender: Gender
    first_name: str
    last_name: str
    cpr: str
    date_of_birth: datetime
    phone_number: str
    address: AddressDTO
