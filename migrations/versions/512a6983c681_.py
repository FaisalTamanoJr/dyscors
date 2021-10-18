"""empty message

Revision ID: 512a6983c681
Revises: 8b78a82f82bb
Create Date: 2021-10-18 19:20:12.529160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '512a6983c681'
down_revision = '8b78a82f82bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_foreign_key(None, 'comment', 'comment', ['parent_comment_id'], ['id'])
    op.drop_column('comment', 'reply_to')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('reply_to', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_foreign_key(None, 'comment', 'comment', ['reply_to'], ['id'])
    # ### end Alembic commands ###
