#!/usr/bin/env python
from flask import Flask, Blueprint
from api.restplus import api
from api.controllers import ns as sentence_namespace

application = Flask(__name__)


def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(sentence_namespace)
    flask_app.register_blueprint(blueprint)

    # db.init_app(flask_app)


def main():
    initialize_app(application)
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
