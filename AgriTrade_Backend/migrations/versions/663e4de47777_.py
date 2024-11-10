"""empty message

Revision ID: 663e4de47777
Revises: de1ca3296c21
Create Date: 2024-02-01 15:01:35.803602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '663e4de47777'
down_revision = 'de1ca3296c21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price_in_cents', sa.Integer(), nullable=False))
        batch_op.drop_column('price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.FLOAT(), nullable=False))
        batch_op.drop_column('price_in_cents')

    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###