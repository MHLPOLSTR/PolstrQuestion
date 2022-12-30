from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Login_Page.html")

@app.route("/question")
def question():
    return render_template("Question_Page.html")

if __name__ == "__main__":
    app.run(debug=True)

