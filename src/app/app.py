from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/app")
def chatbot():
    return render_template("chatbot.html")

if __name__ == "__main__":
    app.run(debug=True)