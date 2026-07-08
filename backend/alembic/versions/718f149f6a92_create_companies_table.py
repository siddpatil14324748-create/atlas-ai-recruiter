"""create companies table

Revision ID: 718f149f6a92
Revises: ee8d6bd456d0
Create Date: 2026-07-07

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "718f149f6a92"
down_revision: Union[str, None] = "ee8d6bd456d0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "companies",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("company_name", sa.String(length=255), nullable=False),
        sa.Column("website", sa.String(length=500), nullable=True),
        sa.Column("linkedin_url", sa.String(length=500), nullable=True),
        sa.Column("industry", sa.String(length=255), nullable=True),
        sa.Column("headquarters", sa.String(length=255), nullable=True),
        sa.Column("company_size", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_companies_company_name",
        "companies",
        ["company_name"],
    )


def downgrade() -> None:
    op.drop_index(
        "ix_companies_company_name",
        table_name="companies",
    )

    op.drop_table("companies")