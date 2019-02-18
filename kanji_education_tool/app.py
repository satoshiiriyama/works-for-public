from flask import Flask, jsonify, render_template, request, make_response
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)