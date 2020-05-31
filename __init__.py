from flask import flask
from flask_bootstrap import Bootstrap
from config import config_options
bootstrap = Bootstrap()
def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    from .main import main as (main_blueprint)

    bootstrap.init_app(app)

    from .request import configure_request
    configure_request(app)

    return app