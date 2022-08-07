from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

posts = requests.get(url=blog_url).json()
post_objects = []

for post in posts:
    post_obj = Post(post_id=post["id"], post_title=post["title"], post_subtitle=post["subtitle"], post_body=post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
