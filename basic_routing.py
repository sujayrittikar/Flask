from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO!<h1>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


# Redirecting
@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route("/<name>admin")
def named_admin(name):
    return redirect(url_for("user", name=name))


if __name__ == "__main__":
    app.run()
