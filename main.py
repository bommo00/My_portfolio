from flask import Flask, render_template, request
import smtplib
import io,sys
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)


#for message
MY_EMAIL = os.environ.get('EMAIL')

MY_PASSWORD = os.environ.get('KEY')

OTHER_EMAIL = os.environ.get('OTHER')




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/artwork")
def gallery():

    return render_template("generic.html")

@app.route("/aboutme",methods=["GET", "POST"])
def self_intro():
    if request.method == 'POST':
        data = request.form
        with smtplib.SMTP("outlook.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            content = f"Subject:A new comment from{data['email_address']}\n\n{data['comment']}"
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=OTHER_EMAIL,
                msg=content
            )
        return render_template("self.html", send=True)

    return render_template("self.html", send=False)

@app.route("/commission")
def prize():
    return render_template("commission.html")


if __name__ == "__main__":
    app.run(debug=True)