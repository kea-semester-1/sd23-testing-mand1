import pytest
from httpx import AsyncClient

URL = "/faker/batch"


@pytest.mark.anyio
async def test_get_batch(client: AsyncClient) -> None:
    """Test getting a batch of faked person data: 200."""

    response = await client.get(URL, params={"size": 10})
    assert response.status_code == 200
    assert response.json() == [{} for _ in range(10)]


@pytest.mark.anyio
async def test_get_batch_with_embeds(client: AsyncClient) -> None:
    """Test getting a batch of faked person data with embeds: 200."""

    embed_params = {
        "size": 3,
        "gender": True,
        "cpr": True,
        "street": False,
    }

    response = await client.get(
        URL,
        params=embed_params,
    )
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 3

    for person in response_json:
        assert len(person) == 2  # gender, cpr
        assert person["gender"] is not None
        assert person["gender"] in {"male", "female"}

        assert person["cpr"] is not None
        assert len(person["cpr"]) == 11  # '-' included


@pytest.mark.anyio
async def test_get_batch_with_embeds_address(client: AsyncClient) -> None:
    """Test getting a batch of data with address attribute embedded: 200."""

    embed_params = {
        "size": 3,
        "gender": False,
        "street": True,
        "number": False,
        "floor": True,
        "postal_code": True,
    }

    response = await client.get(
        URL,
        params=embed_params,
    )
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 3

    for person in response_json:
        assert len(person) == 1  # only address is embedded
        assert len(person["address"]) == 3  # street, floor, postal_code

        assert person["address"]["street"] is not None
        assert person["address"]["floor"] is not None

        assert person["address"]["postal_code"] is not None
        assert len(str(person["address"]["postal_code"])) == 4
