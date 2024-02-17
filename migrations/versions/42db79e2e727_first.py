"""first

Revision ID: 42db79e2e727
Revises: 
Create Date: 2024-01-20 17:34:03.447200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42db79e2e727'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('submenus_count', sa.Integer(), nullable=True),
    sa.Column('dishes_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('submenu',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('dishes_count', sa.Integer(), nullable=True),
    sa.Column('menu_id', sa.Uuid(), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('dish',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('submenu_id', sa.Uuid(), nullable=True),
    sa.ForeignKeyConstraint(['submenu_id'], ['submenu.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dish')
    op.drop_table('submenu')
    op.drop_table('menu')
    # ### end Alembic commands ###