from flask import Flask, render_template, redirect, session, request
from cs50 import SQL
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connecting to database
db = SQL("sqlite:///todo.db")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "todos" not in session:
            session["todos"] = []

        todos = request.form.get("todo")
        session["todos"].append(todos)
        return render_template("index.html", todos=session["todos"])
    else:
        return render_template("index.html")

