from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.numeric import FloatField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'choranene'


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book-library.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(50), nullable=False)
    rating: Mapped[float] = mapped_column(Float(30), nullable=False)


with app.app_context():
    db.create_all()


class BookForm(FlaskForm):
    title = StringField(label="title", validators=[DataRequired()])
    author = StringField(label="author", validators=[DataRequired()])
    rating = FloatField(label="rating", validators=[DataRequired()])
    submit = SubmitField("Add")


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", book_list=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        print(new_book)
        return render_template("add.html", form=form)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
