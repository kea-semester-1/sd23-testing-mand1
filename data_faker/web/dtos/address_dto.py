from pydantic import BaseModel


class AddressDTO(BaseModel):
    """Address DTO."""

    street: str | None = None
    number: str | None = None
    door: str | None = None
    floor: str | None = None
    town: str | None = None
    postal_code: int | None = None
