"""empty message

Revision ID: 0093b4f1eaa1
Revises: 
Create Date: 2020-04-12 21:26:58.046424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0093b4f1eaa1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recriut',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('surname', sa.String(length=20), nullable=True),
    sa.Column('chatname', sa.String(length=20), nullable=True),
    sa.Column('github_name', sa.String(length=80), nullable=True),
    sa.Column('id_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('recriut')
    # ### end Alembic commands ###
