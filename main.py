from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/artwork")
def gallery():
    return render_template("generic.html")

@app.route("/aboutme")
def self_intro():
    return render_template("self.html")

@app.route("/commission")
def prize():
    return render_template("commission.html")


if __name__ == "__main__":
    app.run(debug=True)