import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    VERSION = '0.0.1'

    AWS_REGION = os.environ.get('AWS_REGION')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TABLE_NAME = os.environ.get('TABLE_NAME')

    FONTS_FOLDER = os.path.join(basedir, 'fonts')
    STATIC_FOLDER = os.path.join(basedir, 'app', 'static')

    MAX_CONTENT_LENGTH = 20971520

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
