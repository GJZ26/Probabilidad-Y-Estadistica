import PyE_tools as pye
from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def notFound(error):
    return render_template("notFound.html")

@app.route("/api")
def main():
    return render_template("apiDoc.html")

if(__name__) == "__main__":
    app.run(debug=True)