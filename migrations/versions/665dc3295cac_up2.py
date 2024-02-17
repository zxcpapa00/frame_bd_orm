"""up2

Revision ID: 665dc3295cac
Revises: 19196ee796bc
Create Date: 2024-01-21 13:06:23.759823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '665dc3295cac'
down_revision: Union[str, None] = '19196ee796bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dish', 'price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=True)
    op.drop_constraint('dish_submenu_id_fkey', 'dish', type_='foreignkey')
    op.create_foreign_key(None, 'dish', 'submenu', ['submenu_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('submenu_menu_id_fkey', 'submenu', type_='foreignkey')
    op.create_foreign_key(None, 'submenu', 'menu', ['menu_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'submenu', type_='foreignkey')
    op.create_foreign_key('submenu_menu_id_fkey', 'submenu', 'menu', ['menu_id'], ['id'])
    op.drop_constraint(None, 'dish', type_='foreignkey')
    op.create_foreign_key('dish_submenu_id_fkey', 'dish', 'submenu', ['submenu_id'], ['id'])
    op.alter_column('dish', 'price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=True)
    # ### end Alembic commands ###