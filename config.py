import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'SUPBRO'

ADMIN_USERNAME = 'Matt'

# Yes, this will be hashed if and when this ever goes live
ADMIN_PASSWORD = '12345'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog-dev.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


