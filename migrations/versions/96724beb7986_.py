"""empty message

Revision ID: 96724beb7986
Revises: 75d1f711062a
Create Date: 2020-04-12 23:22:01.067749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96724beb7986'
down_revision = '75d1f711062a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recriut', sa.Column('chort', sa.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recriut', 'chort')
    # ### end Alembic commands ###