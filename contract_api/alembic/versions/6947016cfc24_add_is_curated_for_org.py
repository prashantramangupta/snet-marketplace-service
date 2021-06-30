"""add_is_curated_for_org

Revision ID: 6947016cfc24
Revises: b7e01423560c
Create Date: 2021-06-20 22:40:33.901666

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6947016cfc24'
down_revision = 'b7e01423560c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organization', sa.Column('is_curated', mysql.TINYINT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organization', 'is_curated')
    # ### end Alembic commands ###
