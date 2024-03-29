"""empty message

Revision ID: 48ef0cf6bdf1
Revises: ebec2bcbbbf1
Create Date: 2021-10-16 18:02:09.186992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48ef0cf6bdf1'
down_revision = 'ebec2bcbbbf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gameaccount', 'password')
    op.drop_column('gameaccount', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gameaccount', sa.Column('email', sa.VARCHAR(length=60), autoincrement=False, nullable=True))
    op.add_column('gameaccount', sa.Column('password', sa.VARCHAR(length=512), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
