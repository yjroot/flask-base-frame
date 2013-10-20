from flask import Flask, g
from application.models import Session

blueprints = ['server']


def create_app():
    app = Flask(__name__)
    for name in blueprints:
        app.register_blueprint(load_blueprint(name))

    @app.before_request
    def define_session():
        g.session = Session()
    return app


def load_blueprint(name):
    module = __import__('application.' + name, None, None, ['app'])
    blueprint = getattr(module, 'app')
    return blueprint
