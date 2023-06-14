from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("./website/pages/GroupProject4.html", count=count)

if __name__ == "__main__":
    app.run()
