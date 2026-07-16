from flask import Flask, render_template, request
import db

from cs import (den2bin, den2hex, den2oct, bin2den, hex2den, 
                oct2den, bin2hex, bin2oct, hex2bin, hex2oct)

app = Flask(__name__)


conversions = { 
    "d2b": den2bin, "d2h": den2hex, "d2o": den2oct, "b2d": bin2den, "h2d": hex2den,
    "o2d": oct2den, "b2h": bin2hex, "b2o": bin2oct, "h2b": hex2bin, "h2o": hex2oct
}


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""

    if request.method == "POST":
        conversion = request.form["conversion"]
        number = request.form["number"]

        db.save_input(number)
        answer = conversions[conversion](number)

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