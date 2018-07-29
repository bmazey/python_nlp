from flask import Flask

application = Flask(__name__)


@application.route('/api', methods=['GET'])
def hello():
    return "<p>Hello!</p>"
