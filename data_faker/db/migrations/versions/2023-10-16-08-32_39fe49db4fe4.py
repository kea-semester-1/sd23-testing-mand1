"""empty message

Revision ID: 39fe49db4fe4
Revises: 38b9cff47cdb
Create Date: 2023-10-16 08:32:04.087808

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "39fe49db4fe4"
down_revision = "38b9cff47cdb"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("address_id", sa.UUID(), nullable=False))
    op.drop_constraint("user_address_fkey", "user", type_="foreignkey")
    op.create_foreign_key(None, "user", "address", ["address_id"], ["id"])
    op.drop_column("user", "address")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("address", sa.UUID(), autoincrement=False, nullable=False)
    )
    op.drop_constraint(None, "user", type_="foreignkey")
    op.create_foreign_key("user_address_fkey", "user", "address", ["address"], ["id"])
    op.drop_column("user", "address_id")
    # ### end Alembic commands ###
