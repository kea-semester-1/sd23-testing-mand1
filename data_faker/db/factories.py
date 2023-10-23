import random
from typing import Any, Generic, TypeVar

import factory
from faker import Faker
from pydantic import BaseModel

from data_faker import martin
from data_faker import malthe
from data_faker.db import mo_utils as utils
from data_faker.web.dtos.address_dto import AddressDTO
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO
from data_faker.db.models.models import Address

fake = Faker("da_Dk")
TModel = TypeVar("TModel", bound=BaseModel)


class BaseFactory(Generic[TModel], factory.Factory):
    """
    Base factory.

    Overrides the default create and create_batch methods from Factory, to return
    instances of the associated model, for improved type hinting/auto-completion.
    """

    class Meta:
        abstract = True

    @classmethod
    def create(cls, address_info: Address | None = None, **kwargs: Any) -> TModel:
        """Create an instance of the associated model."""
        if address_info:
            kwargs["address_info"] = address_info
        return cls._generate("create", kwargs)

    @classmethod
    def create_batch(
        cls, size: int, addresses: list[Address] | None = None, **kwargs: Any
    ) -> list[TModel]:
        if addresses:
            return [cls.create(address_info=address, **kwargs) for address in addresses]

        return [cls.create(**kwargs) for _ in range(size)]


class AddressFactory(BaseFactory[AddressDTO]):
    """Address factory."""

    class Meta:
        model = AddressDTO

    street = factory.LazyAttribute(lambda x: malthe.generate_valid_street())
    number = factory.LazyAttribute(lambda x: malthe.generate_number())
    door = factory.LazyAttribute(lambda x: utils.generate_door_value())  # Mo
    floor = factory.LazyAttribute(lambda x: malthe.generate_floor())

    @factory.lazy_attribute
    def town(self) -> str:
        # If the factory has an attribute "address_info"
        if hasattr(self, "address_info") and self.address_info:
            return self.address_info.town
        return str(fake.city_name())

    @factory.lazy_attribute
    def postal_code(self) -> int:
        # If the factory has an attribute "address_info"
        if hasattr(self, "address_info") and self.address_info:
            return self.address_info.postal_code
        return int(fake.postcode())


class FakeInfoFactory(BaseFactory[FakeInfoDTO]):
    """User factory."""

    class Meta:
        model = FakeInfoDTO

    person_info = factory.LazyAttribute(
        lambda _: random.choice(
            malthe.extract_person_info("input_files/person-names.json")
        ),
    )
    first_name = factory.LazyAttribute(lambda x: x.person_info.name)
    last_name = factory.LazyAttribute(lambda x: x.person_info.surname)
    gender = factory.LazyAttribute(lambda x: x.person_info.gender)
    date_of_birth = factory.LazyAttribute(
        lambda _: martin.generate_random_date_of_birth()
    )  # Martin
    cpr = factory.LazyAttribute(
        lambda x: martin.generate_cpr(x.date_of_birth, x.gender),
    )
    phone_number = factory.LazyAttribute(
        lambda _: utils.generate_valid_phone_number(),
    )  # Mo
    address = factory.SubFactory(
        AddressFactory,
        town=factory.SelfAttribute("..address_info.town"),
        postal_code=factory.SelfAttribute("..address_info.postal_code"),
    )
