"""empty message

Revision ID: f9f3d071e6a1
Revises: b97731a27686
Create Date: 2020-04-07 13:47:49.219079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9f3d071e6a1'
down_revision = 'b97731a27686'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('department', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_user_department'), 'user', ['department'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_department'), table_name='user')
    op.drop_column('user', 'department')
    # ### end Alembic commands ###