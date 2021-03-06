"""empty message

Revision ID: 385a5d33bc4c
Revises: 
Create Date: 2018-10-08 15:29:31.619186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '385a5d33bc4c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=128), nullable=True),
    sa.Column('lastname', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_owners_email'), 'owners', ['email'], unique=True)
    op.create_index(op.f('ix_owners_username'), 'owners', ['username'], unique=True)
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('breed', sa.String(length=128), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['owners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('iq', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('dog', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dog'], ['dogs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scores_timestamp'), 'scores', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_scores_timestamp'), table_name='scores')
    op.drop_table('scores')
    op.drop_table('dogs')
    op.drop_index(op.f('ix_owners_username'), table_name='owners')
    op.drop_index(op.f('ix_owners_email'), table_name='owners')
    op.drop_table('owners')
    # ### end Alembic commands ###
