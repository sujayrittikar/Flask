from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<name>")
def user(name):
    return render_template("index.html", content=name, r=2)


# Redirecting
@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route("/<name>admin")
def named_admin(name):
    return redirect(url_for("user", name=name))


if __name__ == "__main__":
    app.run()
