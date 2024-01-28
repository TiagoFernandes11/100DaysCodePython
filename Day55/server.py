from flask import Flask
from random import randint

app = Flask(__name__)

NUMBER_TO_BE_GUESSED = randint(0, 9)


@app.route("/")
def main():
    return ("<h1>Guess a number between 0 and 9</h1><br>"
            '<iframe src="https://giphy.com/embed/IIIg3ZHcOqYtW0wEIB" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/storyful-animals-gorilla-funny-IIIg3ZHcOqYtW0wEIB">via GIPHY</a></p>')


@app.route("/<int:number>")
def number_endpoint(number):
    if number > NUMBER_TO_BE_GUESSED:
        return ("<h1 style='color: purple'>Too high, try again!</h1><br>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    if number < NUMBER_TO_BE_GUESSED:
        return ("<h1 style='color: red'>Too low, try again!</h1><br>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    if number == NUMBER_TO_BE_GUESSED:
        return ("<h1 style='color: green'>You found me!</h1><br>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")


if __name__ == "__main__":
    app.run(debug=True)
