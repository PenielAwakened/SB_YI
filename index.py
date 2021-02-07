from flask import Flask, render_template

app = Flask("bom_project")

@app.route("/")
def index():
    return render_template("index.html")

app.run("127.0.0.1")