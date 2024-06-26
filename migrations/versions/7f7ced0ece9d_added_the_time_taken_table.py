"""added the time_taken table

Revision ID: 7f7ced0ece9d
Revises: 893fc91d96ee
Create Date: 2024-04-11 15:37:45.057263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f7ced0ece9d'
down_revision = '893fc91d96ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Score', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time_taken', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Score', schema=None) as batch_op:
        batch_op.drop_column('time_taken')

    # ### end Alembic commands ###
