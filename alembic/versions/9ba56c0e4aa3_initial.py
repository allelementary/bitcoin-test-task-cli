"""initial

Revision ID: 9ba56c0e4aa3
Revises: 
Create Date: 2024-10-23 22:15:43.369710

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ba56c0e4aa3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'transactions',
        sa.Column('idx', sa.Integer, primary_key=True),
        sa.Column('transaction_id', sa.String, nullable=False),
        sa.Column('inputs', sa.String, nullable=False),
        sa.Column('outputs', sa.String, nullable=False),
        sa.Column('amount', sa.Numeric, nullable=False),
        sa.Column('timestamp', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('transactions')
