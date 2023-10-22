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
    def create(cls, **kwargs: Any) -> TModel:
        """Create an instance of the associated model."""
        return cls._generate("create", kwargs)

    @classmethod
    def create_batch(cls, size: int, **kwargs: Any) -> list[TModel]:
        """Create a batch of instances of the associated model."""
        return [cls.create(**kwargs) for _ in range(size)]


class AddressFactory(BaseFactory[AddressDTO]):
    """Address factory."""

    class Meta:
        model = AddressDTO

    street = factory.LazyAttribute(lambda _: str(fake.street_name()))
    number = factory.LazyAttribute(lambda _: malthe.generate_number())
    door = factory.LazyAttribute(lambda _: str(fake.building_number()))  # Mo
    floor = factory.LazyAttribute(lambda _: malthe.generate_floor())
    town = factory.LazyAttribute(lambda _: str(fake.city_name()))  # Mo
    postal_code = factory.LazyAttribute(lambda x: int(fake.postcode()))  # Mo


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
    address = factory.SubFactory(AddressFactory)  # Martin
