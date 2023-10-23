from pydantic import BaseModel
from datetime import datetime
from data_faker.db.enums import Gender
from data_faker.web.dtos.address_dto import AddressDTO


class FakeInfoDTO(BaseModel):
    """Fake Info DTO."""

    gender: Gender | None = None
    first_name: str | None = None
    last_name: str | None = None
    cpr: str | None = None
    date_of_birth: datetime | None = None
    phone_number: str | None = None
    address: AddressDTO | None = None


class EmbedDTO(BaseModel):
    """DTO for embedding."""

    # Person
    gender: bool = False
    first_name: bool = False
    last_name: bool = False
    cpr: bool = False
    date_of_birth: bool = False
    phone_number: bool = False

    # Address
    street: bool = False
    number: bool = False
    door: bool = False
    floor: bool = False
    town: bool = False
    postal_code: bool = False
