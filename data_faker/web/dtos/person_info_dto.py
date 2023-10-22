from pydantic import BaseModel

from data_faker.db.enums import Gender


class PersonInfoDTO(BaseModel):
    """DTO for person info."""

    name: str
    surname: str
    gender: Gender
