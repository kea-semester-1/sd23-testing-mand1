import json
import string

import factory
from faker import Faker
import random
from typing import Any, Generic, TypeVar
from pydantic import BaseModel
from loguru import logger
from data_faker.web.dtos.address_dto import AddressDTO
from data_faker.web.dtos.fake_info_dto import FakeInfoDTO


fake = Faker("da_Dk")
TModel = TypeVar("TModel", bound=BaseModel)


# TODO: Probably move all helper functions to a separate file
def _generate_phone_number() -> str:
    """Generates a random unique phone number."""
    phone_number = "".join(str(random.randint(2, 7)) for _ in range(8))
    return f"+45{phone_number}"

def generate_number() -> str:
    number = random.randint(1, 999)

    # Decide whether to append an uppercase letter
    if random.choice([True, False]):
        letter = random.choice(string.ascii_uppercase)
        return f"{number}{letter}"
    else:
        return str(number)

def generate_floor() -> Any:
    if random.randint(1, 100) <= 35:
        return "st"
    else:
        return str(random.randint(1, 99))


def extract_person_info() -> dict:
    """
    Extracts the first_name, last_name, and gender from the first object in the persons array in the JSON file.

    Returns:
        dict: A dictionary containing first_name, last_name, and gender of the first person.
    """
    with open("input_files/person-names.json", 'r', encoding="utf-16") as file:
        data = json.load(file)

        # Check if persons array exists and has at least one object
        if 'persons' in data and len(data['persons']) > 0:
            person = random.choice(data['persons'])
            return {
                'first_name': person.get('name', None),
                'last_name': person.get('surname', None),
                'gender': person.get('gender', None)
            }
        else:
            return None

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

    street = factory.LazyAttribute(lambda x: str(fake.street_name()))
    number = factory.LazyAttribute(lambda x: generate_number())
    door = factory.LazyAttribute(lambda x: str(fake.building_number()))  # Mo
    floor = factory.LazyAttribute(lambda x: generate_floor())
    town = factory.LazyAttribute(lambda x: str(fake.city_name()))  # Mo
    postal_code = factory.LazyAttribute(lambda x: int(fake.postcode()))  # Mo


class FakeInfoFactory(BaseFactory[FakeInfoDTO]):
    """User factory."""

    class Meta:
        model = FakeInfoDTO

    person_info = factory.LazyAttribute(lambda x: extract_person_info())
    first_name = factory.LazyAttribute(lambda x: x.person_info["first_name"])
    last_name = factory.LazyAttribute(lambda x: x.person_info["last_name"])
    gender = factory.LazyAttribute(lambda x: x.person_info["gender"])
    cpr = factory.LazyAttribute(lambda x: fake.ssn())  # Martin
    date_of_birth = factory.LazyAttribute(lambda x: fake.date_of_birth())  # Martin
    phone_number = factory.LazyAttribute(lambda x: _generate_phone_number())  # Mo
    address = factory.SubFactory(AddressFactory)  # Martin


wow = [
    "__annotations__",
    "__class__",
    "__deepcopy__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattr__",
    "__getattribute__",
    "__getitem__",
    "__getstate__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__setstate__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "__weakref__",
    "_factories",
    "_factory_map",
    "_locales",
    "_map_provider_method",
    "_optional_proxy",
    "_select_factory",
    "_select_factory_choice",
    "_select_factory_distribution",
    "_unique_proxy",
    "_weights",
    "aba",
    "add_provider",
    "address",
    "administrative_unit",
    "am_pm",
    "android_platform_token",
    "ascii_company_email",
    "ascii_email",
    "ascii_free_email",
    "ascii_safe_email",
    "bank_country",
    "bban",
    "binary",
    "boolean",
    "bothify",
    "bs",
    "building_number",
    "cache_pattern",
    "catch_phrase",
    "century",
    "chrome",
    "city",
    "city_name",
    "city_suffix",
    "color",
    "color_hsl",
    "color_hsv",
    "color_name",
    "color_rgb",
    "color_rgb_float",
    "company",
    "company_email",
    "company_suffix",
    "coordinate",
    "country",
    "country_calling_code",
    "country_code",
    "credit_card_expire",
    "credit_card_full",
    "credit_card_number",
    "credit_card_provider",
    "credit_card_security_code",
    "cryptocurrency",
    "cryptocurrency_code",
    "cryptocurrency_name",
    "csv",
    "currency",
    "currency_code",
    "currency_name",
    "currency_symbol",
    "current_country",
    "current_country_code",
    "date",
    "date_between",
    "date_between_dates",
    "date_object",
    "date_of_birth",
    "date_this_century",
    "date_this_decade",
    "date_this_month",
    "date_this_year",
    "date_time",
    "date_time_ad",
    "date_time_between",
    "date_time_between_dates",
    "date_time_this_century",
    "date_time_this_decade",
    "date_time_this_month",
    "date_time_this_year",
    "day_of_month",
    "day_of_week",
    "del_arguments",
    "dga",
    "dk_street_name",
    "domain_name",
    "domain_word",
    "dsv",
    "ean",
    "ean13",
    "ean8",
    "ein",
    "email",
    "emoji",
    "enum",
    "factories",
    "file_extension",
    "file_name",
    "file_path",
    "firefox",
    "first_name",
    "first_name_female",
    "first_name_male",
    "first_name_nonbinary",
    "fixed_width",
    "format",
    "free_email",
    "free_email_domain",
    "future_date",
    "future_datetime",
    "generator_attrs",
    "get_arguments",
    "get_formatter",
    "get_providers",
    "hex_color",
    "hexify",
    "hostname",
    "http_method",
    "iana_id",
    "iban",
    "image",
    "image_url",
    "internet_explorer",
    "invalid_ssn",
    "ios_platform_token",
    "ipv4",
    "ipv4_network_class",
    "ipv4_private",
    "ipv4_public",
    "ipv6",
    "isbn10",
    "isbn13",
    "iso8601",
    "items",
    "itin",
    "job",
    "json",
    "json_bytes",
    "language_code",
    "language_name",
    "last_name",
    "last_name_female",
    "last_name_male",
    "last_name_nonbinary",
    "latitude",
    "latlng",
    "lexify",
    "license_plate",
    "linux_platform_token",
    "linux_processor",
    "local_latlng",
    "locale",
    "locales",
    "localized_ean",
    "localized_ean13",
    "localized_ean8",
    "location_on_land",
    "longitude",
    "mac_address",
    "mac_platform_token",
    "mac_processor",
    "md5",
    "mime_type",
    "month",
    "month_name",
    "msisdn",
    "name",
    "name_female",
    "name_male",
    "name_nonbinary",
    "nic_handle",
    "nic_handles",
    "null_boolean",
    "numerify",
    "opera",
    "optional",
    "paragraph",
    "paragraphs",
    "parse",
    "passport_dates",
    "passport_dob",
    "passport_full",
    "passport_gender",
    "passport_number",
    "passport_owner",
    "password",
    "past_date",
    "past_datetime",
    "phone_number",
    "port_number",
    "postcode",
    "prefix",
    "prefix_female",
    "prefix_male",
    "prefix_nonbinary",
    "pricetag",
    "profile",
    "provider",
    "providers",
    "psv",
    "pybool",
    "pydecimal",
    "pydict",
    "pyfloat",
    "pyint",
    "pyiterable",
    "pylist",
    "pyobject",
    "pyset",
    "pystr",
    "pystr_format",
    "pystruct",
    "pytimezone",
    "pytuple",
    "random",
    "random_choices",
    "random_digit",
    "random_digit_above_two",
    "random_digit_not_null",
    "random_digit_not_null_or_empty",
    "random_digit_or_empty",
    "random_element",
    "random_elements",
    "random_int",
    "random_letter",
    "random_letters",
    "random_lowercase_letter",
    "random_number",
    "random_sample",
    "random_uppercase_letter",
    "randomize_nb_elements",
    "rgb_color",
    "rgb_css_color",
    "ripe_id",
    "safari",
    "safe_color_name",
    "safe_domain_name",
    "safe_email",
    "safe_hex_color",
    "sbn9",
    "seed",
    "seed_instance",
    "seed_locale",
    "sentence",
    "sentences",
    "set_arguments",
    "set_formatter",
    "sha1",
    "sha256",
    "simple_profile",
    "slug",
    "ssn",
    "state",
    "street_address",
    "street_name",
    "street_suffix",
    "suffix",
    "suffix_female",
    "suffix_male",
    "suffix_nonbinary",
    "swift",
    "swift11",
    "swift8",
    "tar",
    "text",
    "texts",
    "time",
    "time_delta",
    "time_object",
    "time_series",
    "timezone",
    "tld",
    "tsv",
    "unique",
    "unix_device",
    "unix_partition",
    "unix_time",
    "upc_a",
    "upc_e",
    "uri",
    "uri_extension",
    "uri_page",
    "uri_path",
    "url",
    "user_agent",
    "user_name",
    "uuid4",
    "vin",
    "weights",
    "windows_platform_token",
    "word",
    "words",
    "xml",
    "year",
    "zip",
]
