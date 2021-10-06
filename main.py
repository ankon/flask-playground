from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/browse/<name>")
def index(name):
    return render_template('index.html.jinja', name=name)
