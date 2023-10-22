import pytest

from data_faker.db.factories import AddressFactory
from data_faker.web.dtos.address_dto import AddressDTO


@pytest.mark.parametrize(
    "attribute", ["street", "number", "door", "floor", "town", "postal_code"]
)
def test_address_factory_attribute(attribute: str) -> None:
    """Test each attribute of the address_factory."""
    address = AddressFactory.create()
    assert isinstance(address, AddressDTO)

    if attribute == "postal_code":
        value = getattr(address, attribute)
        assert isinstance(value, int)
        assert value > 0
        return

    value = getattr(address, attribute)
    assert isinstance(value, str)
    assert len(value) > 0
