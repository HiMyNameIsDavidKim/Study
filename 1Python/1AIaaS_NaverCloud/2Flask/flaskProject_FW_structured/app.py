import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def hello_world():
    return render_template("hello.html")

@app.route("/users/<username>")
def get_user(username):
    return username

@app.route("/posts/<int:post_id>")
def get_post(post_id):
    return str(post_id)

@app.route("/uuid/<uuid:uuid>")
def get_uuid(uuid):
    return str(uuid)

@app.route("/login", methods=["GET","POST"])
def login_page():
    if request.method == "POST":
        return "로그인 성공"
    else:
        return "로그인 화면"


if __name__=="__main__":
    # app.run()
    df = pd.read_csv("./static/save/cop/scp/bugs_ranking.csv")
    print(" ### ")
    print(df)