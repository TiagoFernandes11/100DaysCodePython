from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        return "<h1><b>" + function() + "</b></h1>"

    return bold


@app.route("/")
def hello_world():
    return '<h1 style= "text-align: center">Hello, World!</h1>'


@app.route("/bye")
@make_bold
def bye():
    return "bye!"


@app.route("/username/<name>/<int:number>")
def hello_user(name, number):
    return f"<p>Hello, {name}! {number}</p>"


if __name__ == "__main__":
    app.run(debug=True)
