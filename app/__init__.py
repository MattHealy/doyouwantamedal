import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

from werkzeug.contrib.fixers import ProxyFix

from config import config, basedir

bootstrap = Bootstrap()

csrf = CSRFProtect()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    csrf.init_app(app)

    from . main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    if not os.path.exists(os.path.join(basedir, 'tmp')):
        os.makedirs(os.path.join(basedir, 'tmp'))

    if config_name == 'development':
        import logging
        from logging.handlers import RotatingFileHandler

        file_handler = RotatingFileHandler('tmp/medal.log',
                                           'a', 1 * 1024 * 1024, 10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s \
             [in %(pathname)s:%(lineno)d]'))
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('medal startup')

    return app
