"""empty message

Revision ID: e6be1dfb2948
Revises: 0aeb82f525e7
Create Date: 2023-05-15 14:06:28.892863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6be1dfb2948'
down_revision = '0aeb82f525e7'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_pyduck():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer_vote')
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('answer_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_vote_answer_id_answer'), 'answer', ['answer_id'], ['id'])

    # ### end Alembic commands ###


def downgrade_pyduck():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_vote_answer_id_answer'), type_='foreignkey')
        batch_op.drop_column('answer_id')

    op.create_table('answer_vote',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.VARCHAR(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('answer_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['answer_id'], ['answer.id'], name='fk_answer_vote_answer_id_answer'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_answer_vote_user_id_user'),
    sa.PrimaryKeyConstraint('id', name='pk_answer_vote')
    )
    # ### end Alembic commands ###


def upgrade_faduck():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_faduck():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

