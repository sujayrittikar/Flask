from flask import (
    Flask, render_template, request,
    redirect, url_for, session, flash
)
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "W8BssY228T1"
app.permanent_session_lifetime = timedelta(seconds=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        if user:
            return redirect(url_for("user"))
        else:
            return "No User Entered"
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        usr = session["user"]
        return f"<h1>{usr}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You're logged out!", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)