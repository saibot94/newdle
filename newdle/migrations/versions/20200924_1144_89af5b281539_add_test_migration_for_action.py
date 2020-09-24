"""Add test migration for action

Revision ID: 89af5b281539
Revises: 43f0bf77bf97
Create Date: 2020-09-24 11:44:50.773016
"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '89af5b281539'
down_revision = '43f0bf77bf97'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'newdles',
        sa.Column('test_column', sa.String(), server_default='', nullable=False),
    )


def downgrade():
    op.drop_column('newdles', 'test_column')
