from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def index():
  return render_template("about.html")

@app.route("/contact")
def index():
  return render_template("contact.html")


app.run(debug=True)