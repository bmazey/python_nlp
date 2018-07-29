#!/usr/bin/env python

from flask import Flask

application = Flask(__name__)


@application.route('/api', methods=['GET'])
def hello():
    return "<p>Hello!</p>"


if __name__ == "__main__":
    application.debug = True
    application.run()
