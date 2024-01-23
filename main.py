from flask import Flask, render_template
from post import Post
import requests


def request_dummy_blog_posts():
    dummy_blogs_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    dummy_blogs_response.raise_for_status()
    dummy_blogs = dummy_blogs_response.json()

    dummy_blogs_list = []
    for blog in dummy_blogs:
        post = Post(blog)
        dummy_blogs_list.append(post)
    return dummy_blogs_list


posts_list = request_dummy_blog_posts()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=posts_list)


@app.route('/post/<int:blog_id>')
def display_post(blog_id):
    post_position = blog_id - 1
    return render_template('post.html', post=posts_list[post_position])


if __name__ == "__main__":
    app.run(debug=True)
