"""Adding unique id to contributions.

Revision ID: 9ed4811a814d
Revises: 4e6299081e3f
Create Date: 2020-03-03 21:18:57.710336

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9ed4811a814d'
down_revision = '4e6299081e3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('individual_contribution', sa.Column('fec_unique_id', sa.Numeric(precision=19), nullable=False))
    op.create_unique_constraint(None, 'individual_contribution', ['fec_unique_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'individual_contribution', type_='unique')
    op.drop_column('individual_contribution', 'fec_unique_id')
    # ### end Alembic commands ###
