"""Add fake migration

Revision ID: 4f2ded290132
Revises: 43f0bf77bf97
Create Date: 2020-09-29 09:24:38.710150
"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '4f2ded290132'
down_revision = '43f0bf77bf97'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'newdles', sa.Column('fake_col', sa.String(), server_default='', nullable=False)
    )


def downgrade():
    op.drop_column('newdles', 'fake_col')
