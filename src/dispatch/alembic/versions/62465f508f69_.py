"""Adding dispatch user table

Revision ID: 62465f508f69
Revises: 1221a4d60f03
Create Date: 2020-04-21 15:24:55.512154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "62465f508f69"
down_revision = "895ae7783033"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "dispatch_user",
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.Binary(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("dispatch_user")
    # ### end Alembic commands ###