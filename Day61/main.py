from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(message="Email is required"), validators.email("Insert a valid email")])
    password = PasswordField(label='Password', validators=[DataRequired("Password is required")])
    submit = SubmitField(label="Log in")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
