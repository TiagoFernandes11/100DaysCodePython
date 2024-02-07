from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db.init_app(app)


class TaskForm(FlaskForm):
    title = StringField("Todo Task Title", validators=[DataRequired()])
    description = StringField("Todo Task Description", validators=[DataRequired()])
    submit = SubmitField("Submit Task")


class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    tasks = db.session.execute(db.select(Task).order_by(Task.id)).scalars()
    return render_template("home.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add-task.html", form=form)


@app.route("/task/<int:id>/delete", methods=["GET", "POST"])
def delete_task(id):
    task = db.get_or_404(Task, id)
    db.session.delete(task)
    db.session.commit()
    return index()


if __name__ == "__main__":
    app.run(debug=True)
