"""empty message

Revision ID: af2eec17605f
Revises: 97716853cddf
Create Date: 2020-06-16 19:58:31.908272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af2eec17605f'
down_revision = '97716853cddf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answer', 'answerString',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint('answer_question_id_fkey', 'answer', type_='foreignkey')
    op.drop_column('answer', 'question_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('question_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('answer_question_id_fkey', 'answer', 'question', ['question_id'], ['id'])
    op.alter_column('answer', 'answerString',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
