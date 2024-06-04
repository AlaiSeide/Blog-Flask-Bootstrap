from alembic import op
import sqlalchemy as sa

# Revisão e revisão descendente
revision = '8e17de138de7'
down_revision = '3dbabbdfae84'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=128), nullable=False))
        batch_op.create_unique_constraint('uq_user_email', ['email'])  # Nome da restrição adicionado

def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('uq_user_email', type_='unique')
        batch_op.drop_column('email')
