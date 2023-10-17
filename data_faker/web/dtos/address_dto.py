from pydantic import BaseModel


class AddressDTO(BaseModel):
    """Address DTO."""

    street: str
    number: str
    door: str
    floor: str
    town: str
    postal_code: int
