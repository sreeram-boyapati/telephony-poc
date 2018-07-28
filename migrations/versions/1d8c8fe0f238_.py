"""empty message

Revision ID: 1d8c8fe0f238
Revises: 
Create Date: 2018-07-28 19:36:03.271382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d8c8fe0f238'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender', sa.String(length=16), nullable=True),
    sa.Column('receiver', sa.String(length=16), nullable=True),
    sa.Column('sms_text', sa.String(length=120), nullable=True),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sms_receiver'), 'sms', ['receiver'], unique=False)
    op.create_index(op.f('ix_sms_sender'), 'sms', ['sender'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sms_sender'), table_name='sms')
    op.drop_index(op.f('ix_sms_receiver'), table_name='sms')
    op.drop_table('sms')
    # ### end Alembic commands ###
