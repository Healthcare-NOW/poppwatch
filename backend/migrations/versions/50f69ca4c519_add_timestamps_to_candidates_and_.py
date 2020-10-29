"""Add timestamps to candidates and committees.

Revision ID: 50f69ca4c519
Revises: 4b50d4e762a5
Create Date: 2020-07-20 13:56:58.068404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f69ca4c519'
down_revision = '4b50d4e762a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('candidate', sa.Column('created_at', sa.DateTime(), server_default=sa.text("now() at time zone 'utc'"), nullable=False))
    op.add_column('candidate', sa.Column('updated_at', sa.DateTime(), server_default=sa.text("now() at time zone 'utc'"), nullable=False))
    op.add_column('committee', sa.Column('created_at', sa.DateTime(), server_default=sa.text("now() at time zone 'utc'"), nullable=False))
    op.add_column('committee', sa.Column('updated_at', sa.DateTime(), server_default=sa.text("now() at time zone 'utc'"), nullable=False))
    op.drop_constraint('individual_contributor_flagged_as_id_fkey', 'individual_contributor', type_='foreignkey')
    op.drop_column('individual_contributor', 'flagged_as_id')
    op.drop_table('flagged_individual_contributor')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flagged_individual_contributor',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=2), autoincrement=False, nullable=True),
    sa.Column('zip', sa.VARCHAR(length=9), autoincrement=False, nullable=True),
    sa.Column('occupation', sa.VARCHAR(length=38), autoincrement=False, nullable=True),
    sa.Column('flagged_employer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['flagged_employer_id'], ['flagged_employer.id'], name='flagged_individual_contributor_flagged_employer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='flagged_individual_contributor_pkey')
    )
    op.add_column('individual_contributor', sa.Column('flagged_as_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('individual_contributor_flagged_as_id_fkey', 'individual_contributor', 'flagged_individual_contributor', ['flagged_as_id'], ['id'])
    op.drop_column('committee', 'updated_at')
    op.drop_column('committee', 'created_at')
    op.drop_column('candidate', 'updated_at')
    op.drop_column('candidate', 'created_at')
    # ### end Alembic commands ###
