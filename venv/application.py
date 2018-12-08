from flask import Flask, render_template, url_for, request  # Import the class `Flask` from the `flask` module, written by someone else.

app = Flask(__name__)  # Instantiate a new web application called `app`, with `__name__` representing the current file


@app.route("/")  # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")