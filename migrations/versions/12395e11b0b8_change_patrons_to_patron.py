"""change_patrons_to_patron

Revision ID: 12395e11b0b8
Revises: 4068f2448893
Create Date: 2018-06-21 14:26:28.998160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12395e11b0b8'
down_revision = '4068f2448893'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patron',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('surname', sa.String(length=60), nullable=True),
    sa.Column('id_number', sa.String(length=20), nullable=True),
    sa.Column('initials', sa.String(length=10), nullable=True),
    sa.Column('suburb', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=30), nullable=True),
    sa.Column('postal_code', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('alternative_phone', sa.String(length=15), nullable=True),
    sa.Column('next_of_kin', sa.String(length=100), nullable=True),
    sa.Column('next_of_kin_relation', sa.String(length=30), nullable=True),
    sa.Column('next_of_kin_contact', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_patron_email'), 'patron', ['email'], unique=False)
    op.create_index(op.f('ix_patron_id_number'), 'patron', ['id_number'], unique=False)
    op.create_index(op.f('ix_patron_name'), 'patron', ['name'], unique=False)
    op.create_index(op.f('ix_patron_surname'), 'patron', ['surname'], unique=False)
    op.drop_index('ix_patrons_email', table_name='patrons')
    op.drop_index('ix_patrons_id_number', table_name='patrons')
    op.drop_index('ix_patrons_name', table_name='patrons')
    op.drop_index('ix_patrons_surname', table_name='patrons')
    op.drop_table('patrons')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patrons',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('surname', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.Column('id_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('initials', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('suburb', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('postal_code', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('alternative_phone', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('next_of_kin', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('next_of_kin_relation', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('next_of_kin_contact', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='patrons_pkey')
    )
    op.create_index('ix_patrons_surname', 'patrons', ['surname'], unique=False)
    op.create_index('ix_patrons_name', 'patrons', ['name'], unique=False)
    op.create_index('ix_patrons_id_number', 'patrons', ['id_number'], unique=False)
    op.create_index('ix_patrons_email', 'patrons', ['email'], unique=False)
    op.drop_index(op.f('ix_patron_surname'), table_name='patron')
    op.drop_index(op.f('ix_patron_name'), table_name='patron')
    op.drop_index(op.f('ix_patron_id_number'), table_name='patron')
    op.drop_index(op.f('ix_patron_email'), table_name='patron')
    op.drop_table('patron')
    # ### end Alembic commands ###
