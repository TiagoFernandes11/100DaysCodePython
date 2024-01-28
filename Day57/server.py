from flask import Flask, render_template
import requests
from datetime import date

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html", CURRENT_YEAR=date.today().year)


@app.route("/guess/<name>")
def guess(name):
    age_data = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender_data = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("guess.html", name=str.upper(name[0]) + name[1:], age_data=str(age_data), gender_data=str(gender_data))


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
