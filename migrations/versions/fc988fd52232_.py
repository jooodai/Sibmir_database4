"""empty message

Revision ID: fc988fd52232
Revises: 0fe34a61ce9e
Create Date: 2020-04-06 21:07:35.875597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc988fd52232'
down_revision = '0fe34a61ce9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('fio', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_user_fio'), 'user', ['fio'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_fio'), table_name='user')
    op.drop_column('user', 'fio')
    # ### end Alembic commands ###