from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def root():
    return redirect("https://github.com/Mews/crossroad-finder-api")


if __name__ == "__main__":
    app.run()
