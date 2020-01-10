import flask

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return flask.render_template("index.html", token='Flask+React')
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
