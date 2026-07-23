"""Add page_count to invoices

Revision ID: f2f3f4b5c6d7
Revises: d56af1e21443
Create Date: 2026-07-23 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2f3f4b5c6d7'
down_revision: Union[str, Sequence[str], None] = 'd56af1e21443'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('invoices', sa.Column('page_count', sa.Integer(), nullable=True, server_default='0'))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('invoices', 'page_count')
