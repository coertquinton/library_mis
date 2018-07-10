"""patron_table_add_created_and_modified

Revision ID: d259a9b36d3a
Revises: 12395e11b0b8
Create Date: 2018-06-21 14:46:45.229941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd259a9b36d3a'
down_revision = '12395e11b0b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patron', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.add_column('patron', sa.Column('last_updated', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patron', 'last_updated')
    op.drop_column('patron', 'created_on')
    # ### end Alembic commands ###
