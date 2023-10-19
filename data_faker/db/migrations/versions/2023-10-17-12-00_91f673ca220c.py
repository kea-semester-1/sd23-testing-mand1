"""empty message

Revision ID: 91f673ca220c
Revises: 39fe49db4fe4
Create Date: 2023-10-17 12:00:38.520641

"""
import sqlalchemy as sa
from alembic import op
import sqlparse

# revision identifiers, used by Alembic.
revision = "91f673ca220c"
down_revision = "39fe49db4fe4"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("address", "street")
    op.drop_column("address", "number")
    op.drop_column("address", "floor")
    op.drop_column("address", "door")
    op.drop_constraint("user_address_id_fkey", "user", type_="foreignkey")
    op.drop_column("user", "address_id")
    # ### end Alembic commands ###
    with open("./input_files/addresses.sql", "r") as f:
        sql_commands = f.read()

    # Using sqlparse to split the commands
    for cmd in sqlparse.split(sql_commands):
        if cmd.strip():  # ensuring no empty command is executed
            op.execute(cmd)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("address_id", sa.UUID(), autoincrement=False, nullable=False)
    )
    op.create_foreign_key(
        "user_address_id_fkey", "user", "address", ["address_id"], ["id"]
    )
    op.add_column(
        "address",
        sa.Column("door", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    )
    op.add_column(
        "address",
        sa.Column("floor", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    )
    op.add_column(
        "address",
        sa.Column(
            "number", sa.VARCHAR(length=255), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "address",
        sa.Column(
            "street", sa.VARCHAR(length=255), autoincrement=False, nullable=False
        ),
    )
    # ### end Alembic commands ###
