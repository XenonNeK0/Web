from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s!" % name


@app.route("/blog/<int:postID>")
def show_blog(postID):
    return "Blig Number %d" % postID


@app.route("/rev/<float:revNo>")
def revision(revNo):
    return "Revision Number %f" % revNo


if __name__ == "__main__":
    app.run(debug=True)
