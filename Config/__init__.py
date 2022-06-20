class Config(object):
    # set parameter for Mysql, actually, it's recommended to store those parameter in the environment variable
    user = '******'
    password = '******'
    database = '******'
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user, password, database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

    # set the secret key, similarly, it's recommended to store those parameter in the environment variable
    SECRET_KEY = "******"
