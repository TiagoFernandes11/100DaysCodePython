from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:num>")
def get_post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    post = requests.get(blog_url).json()[num - 1]
    return render_template("post.html", post=post, id=num)


if __name__ == "__main__":
    app.run(debug=True)
