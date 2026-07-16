from flask import Flask, render_template, request
import db

from cs import CONVERSIONS

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""

    if request.method == "POST":
        conversion = request.form["conversion"]
        number = request.form["number"]

        db.save_input(number)
        answer = CONVERSIONS[conversion](number)

    return render_template(
        "home.html",
        answer=str(answer).upper(),
    )


@app.route("/history")
def history():
    return render_template(
        "history.html",
        recent_inputs=db.recent_input(21)
    )


if __name__ == "__main__":
    app.run(debug=True)