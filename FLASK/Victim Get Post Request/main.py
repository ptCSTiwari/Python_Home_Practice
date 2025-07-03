#this flask main file did not crates any seprate file for inputted text

from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route('/')
# def index():
#   return render_template(index.html)

@app.route("/", methods=["GET", "POST"])
def contact():
  print(request.method)
  print(request.form)
  return render_template("contact.html")

if __name__ == '__main__':
  app.run(debug=True)