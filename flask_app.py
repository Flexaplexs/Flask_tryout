from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Welkom bij mijn eerste Flask-website!</p>"