import time
import os
from flask import Flask
from database import db
from .models import User
from .routes import bp


def create_app(**kwargs):
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config.from_object('config.Appication')

    db.init_app(app)

    with app.app_context():

        # wait for the database to load
        if 'DOCKER_CONTAINER' in os.environ:
            time.sleep(15)

        db.create_all()
        return app
