"""empty message

Revision ID: 64a1b1538989
Revises: 
Create Date: 2018-09-10 13:08:21.376987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64a1b1538989'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('u_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('u_name', sa.String(length=16), nullable=True),
    sa.Column('_u_password', sa.String(length=256), nullable=True),
    sa.Column('u_permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('u_id'),
    sa.UniqueConstraint('u_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
