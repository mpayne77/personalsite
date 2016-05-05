from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
blog_post = Table('blog_post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=200)),
    Column('subtite', VARCHAR(length=200)),
    Column('slug', VARCHAR(length=200)),
    Column('thumbnail', TEXT),
    Column('content', TEXT),
    Column('author', VARCHAR(length=100)),
)

blog_post = Table('blog_post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=200)),
    Column('subtitle', String(length=200)),
    Column('slug', String(length=200)),
    Column('thumbnail', Text),
    Column('content', Text),
    Column('author', String(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['blog_post'].columns['subtite'].drop()
    post_meta.tables['blog_post'].columns['subtitle'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['blog_post'].columns['subtite'].create()
    post_meta.tables['blog_post'].columns['subtitle'].drop()
