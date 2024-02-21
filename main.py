import flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='templates')


@app.route("/")
def index():
  return render_template("home.html")
@app.route("/unverified")
def unverified():
  return render_template("unverified.html")
@app.route("/verified")
def verified():
  return render_template("verified.html")
@app.route("/search")
if __name__ == "__main__":
  app.run(debug = True,port=8080)