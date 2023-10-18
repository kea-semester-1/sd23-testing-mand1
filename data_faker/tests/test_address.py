import pytest
from data_faker.db.dao.address_dao import AddressDAO
from sqlalchemy.ext.asyncio import AsyncSession
import sqlparse
import sqlalchemy as sa


@pytest.mark.anyio
async def test_get_address(dbsession: AsyncSession) -> None:
    address = AddressDAO(dbsession)

    with open("./input_files/addresses.sql", "r") as f:
        sql_commands = f.read()

    # Using sqlparse to split the commands
    for cmd in sqlparse.split(sql_commands):
        if cmd.strip():  # ensuring no empty command is executed
            await dbsession.execute(sa.text(cmd))
    # ### end Alembic commands ###
    address_1 = await address.get_random_row()

    print(address_1)
