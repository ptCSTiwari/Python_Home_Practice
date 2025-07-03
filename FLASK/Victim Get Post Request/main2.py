#this flask main file creates any seprate file for inputted text

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
  if(request.method == "POST"):
    with open("data.txt", "w") as f:
      f.write(f"The name of the victim is {request.form['name']},\n email of the victim is {request.form['email']},\n final message from the victim is {'message'}")
      return render_template("contact.html")
  return render_template("contact.html")

if __name__ == '__main__':
  app.run(debug=True)