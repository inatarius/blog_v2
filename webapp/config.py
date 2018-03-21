class Config(object):
    SECRET_KEY = '1f4e0fe02ca8d5a258b0c996a0b471e0'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/blog_v2"