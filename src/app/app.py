from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app")
def chatbot():
    return render_template("chatbot.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/api-route/send-message", methods=["POST"])
def send_message():
    return request.form

if __name__ == "__main__":
    app.run(debug=True)