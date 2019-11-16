"""empty message

Revision ID: 331b01916949
Revises: 
Create Date: 2019-11-12 17:49:13.204757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '331b01916949'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('numFollowers', sa.Integer(), nullable=True),
    sa.Column('numFollowing', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username'),
    sqlite_autoincrement=True
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('num_likes', sa.Integer(), nullable=True),
    sa.Column('num_comments', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('of', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['of'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('like_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('liked_by', sa.Integer(), nullable=True),
    sa.Column('liked_post', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['liked_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['liked_post'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('liked_by'),
    sa.UniqueConstraint('liked_by', 'liked_post', name='unique_like'),
    sa.UniqueConstraint('liked_post')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like_post')
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('user')
    # ### end Alembic commands ###