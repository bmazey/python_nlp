#!/usr/bin/env python
# import sys
# sys.path.insert(0, "/api")

# ignore pep complaints
from flask import Flask, Blueprint
from .restplus import api
from .controllers import ns as sentence_namespace


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
    # print(sys.path)
