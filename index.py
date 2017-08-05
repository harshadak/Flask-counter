from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Secret"

@app.route("/")
def index():
    session["count"] += 1
    return render_template("index.html")

@app.route("/add", methods = ["POST"])
def addByTwo():
    session["count"] += 2
    return render_template("index.html")
    return redirect("/")

@app.route("/reset", methods = ["POST"])
def resetCounter():
    session["count"] = 0
    return render_template("index.html")
    return redirect("/")

app.run(debug = True)