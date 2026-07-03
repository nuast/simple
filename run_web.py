from flask import Flask, render_template, request
import db # import save
from conv import bin2hex

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""

    if request.method == "POST":
        binary = request.form["binary"]
        db.save_input(binary)  # save.save_input(binary)
        answer = bin2hex(binary)

    return render_template("index.html", answer=answer.upper(), recent_inputs=db.recent_input()) #save.recent_input()

if __name__ == "__main__":
    app.run(debug=True)