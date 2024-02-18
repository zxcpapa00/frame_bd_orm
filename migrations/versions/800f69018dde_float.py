"""float

Revision ID: 800f69018dde
Revises: 665dc3295cac
Create Date: 2024-02-18 20:42:24.640018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '800f69018dde'
down_revision: Union[str, None] = '665dc3295cac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
