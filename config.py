import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'my_database_3',
        'host': 'localhost',
        'port': '5432',
    }

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_never_guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False

