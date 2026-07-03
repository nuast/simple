from flask import Flask, render_template, request
from conv import bin2hex

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""

    if request.method == "POST":
        binary = request.form["binary"]
        answer = bin2hex(binary)

    return render_template("index.html", answer=answer.upper(), recent_inputs=db.recent_input())

if __name__ == "__main__":
    app.run(debug=True)