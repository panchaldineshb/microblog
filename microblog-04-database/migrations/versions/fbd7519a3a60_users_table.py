"""users table

Revision ID: fbd7519a3a60
Revises: cadf4693ad72
Create Date: 2018-10-08 14:55:53.994364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbd7519a3a60'
down_revision = 'cadf4693ad72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('confirmed', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'name')
    op.drop_column('user', 'member_since')
    op.drop_column('user', 'location')
    op.drop_column('user', 'confirmed')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
