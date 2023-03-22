"""add token to user

Revision ID: 4fa0646d2a53
Revises: 6cf5f5fd0f7e
Create Date: 2022-09-16 20:44:09.263444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fa0646d2a53'
down_revision = '6cf5f5fd0f7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('token_cookie', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'token_cookie')
    # ### end Alembic commands ###
