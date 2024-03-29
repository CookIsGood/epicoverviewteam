"""Initial migration.

Revision ID: b2ddb0764945
Revises: 
Create Date: 2021-10-16 17:51:26.144708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ddb0764945'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gameaccount', sa.Column('email', sa.String(length=60), nullable=False))
    op.add_column('gameaccount', sa.Column('password', sa.String(length=512), nullable=False))
    op.create_unique_constraint(None, 'gameaccount', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gameaccount', type_='unique')
    op.drop_column('gameaccount', 'password')
    op.drop_column('gameaccount', 'email')
    # ### end Alembic commands ###
