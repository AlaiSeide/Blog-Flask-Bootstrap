"""Add senha to User model

Revision ID: e3df57a685a2
Revises: 8e17de138de7
Create Date: 2024-06-04 13:48:42.730935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3df57a685a2'
down_revision = '8e17de138de7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.String(length=128), nullable=False))
        batch_op.create_unique_constraint(None, ['senha'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('senha')

    # ### end Alembic commands ###