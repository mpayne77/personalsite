import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'SUPBRO'

# Currently I'm envisioning myself as the only person allowed to upload content
# so I'm skipping a 'Users' table in the database.
ADMIN_USERNAME = 'Matt'
ADMIN_PASSWORD = '$5$rounds=535000$G61/o0QD8ZTaJvhE$Q8/JCCRAqUyEbiiM2o61jw6sEd8Vx2/L5Ywpn/9FnvA'

ADMIN_MODE = False

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog-dev.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_TRACK_MODIFICATIONS = False
