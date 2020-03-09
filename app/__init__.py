from flask import Flask
from config import Config
from app.database import db
from app.serialization import ma
from flask_migrate import Migrate
from app.routes import handlers
from app.api import api


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.register_blueprint(handlers)
    app.register_blueprint(api)
    db.init_app(app)
    ma.init_app(app)
    return app


app = create_app()

migrate = Migrate(app, db, compare_type=True)
