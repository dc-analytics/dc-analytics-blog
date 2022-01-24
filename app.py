from flask import Flask



app = Flask(__name__)


@app.route("/test/<test>")
def index(test='nothing yet'):
    return test


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

