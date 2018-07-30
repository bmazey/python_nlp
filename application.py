from flask import Flask


application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
    # print(sys.path)
