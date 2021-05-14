from flask import Flask, request, render_template

from src import solver

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("solve.html")


@app.route("/solve", methods=["POST"])
def solve():
    try:
        letters = request.form["letters"]
        letters = letters.lower().strip()
    except:
        letters = "... konnts nicht auslesen. :("
        return render_template("solved.html", letters=letters, ger="", eng="")
    list = solver.split(letters)
    german_word = solver.check_german(list)
    englisch_word = solver.check_english(list)
    return render_template(
        "solved.html", letters=letters, ger=german_word, eng=englisch_word
    )


@app.route("/impressum")
def impressum():
    return render_template("impressum.html")


if __name__ == "__main__":
    app.run(debug=True)
