import pytest
from httpx import AsyncClient

URL = "/faker/single"


@pytest.mark.anyio
async def test_get_single(client: AsyncClient) -> None:
    """Test getting a single faked person data: 200."""

    response = await client.get(URL)
    assert response.status_code == 200
    assert response.json() == {}


@pytest.mark.anyio
async def test_get_single_with_embeds(client: AsyncClient) -> None:
    """Test getting a single faked person data with embeds: 200."""

    embed_params = {
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

    assert "address" not in response_json  # street is False, so no address

    assert response_json["gender"] is not None
    assert response_json["gender"] in {"male", "female"}

    assert response_json["cpr"] is not None
    assert len(response_json["cpr"]) == 11  # '-' included


@pytest.mark.anyio
async def test_get_single_with_embeds_address(client: AsyncClient) -> None:
    """Test getting a single faked person data with address attribute embedded: 200."""

    embed_params = {
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

    assert len(response_json) == 1  # only address is embedded
    assert len(response_json["address"]) == 3  # street, floor, postal_code

    assert response_json["address"]["street"] is not None
    assert response_json["address"]["floor"] is not None

    assert response_json["address"]["postal_code"] is not None
    assert len(str(response_json["address"]["postal_code"])) == 4
