from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.numeric import FloatField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'choranene'

all_books = []


class BookForm(FlaskForm):
    title = StringField(label="title", validators=[DataRequired()])
    author = StringField(label="author", validators=[DataRequired()])
    rating = FloatField(label="rating", validators=[DataRequired()])
    submit = SubmitField("Add")


@app.route('/')
def home():
    return render_template("index.html", book_list=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        all_books.append({
            "title": title,
            "author": author,
            "rating": rating
        })
        print(all_books)
        return render_template("add.html", form=form)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
