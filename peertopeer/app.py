from flask import Flask, render_template,uest, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("principal.html")

if __name__ == "__main__":
    app.run(debug=True)