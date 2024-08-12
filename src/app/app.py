import os
import sys

sys.path.append(os.path.abspath("./src"))

from gemini.load_creds import load_creds

from flask import *
import google.generativeai as genai

load_creds()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", mode=session.get("mode"))

@app.route("/app")
def chatbot():
    model_lst = genai.list_tuned_models()
    
    return render_template("chatbot.html", mode=session.get("mode"), model_lst=model_lst)

@app.route("/map")
def map():
    return render_template("map.html", mode=session.get("mode"))

@app.route(f"/api-route/", methods=["POST"])
def api_route():
    return Response(200, "Received")

@app.route(f"/api-route/mode-pref", methods=["POST"])
def mode_pref():
    session["mode"] = request.form.get("mode")
    print(session["mode"])
    return Response(200)

@app.route(f"/api-route/<model_name>/model-info", methods=["POST"])
def model_info(model_name):
    model = genai.get_tuned_model(f"tunedModels/{model_name}")
    
    return jsonify(model)

@app.route(f"/api-route/<model_name>/send-message", methods=["POST"])
def send_message(model_name):
    model = genai.GenerativeModel(model_name)

    # config options : stop_sequences, candidate_count, max_output_tokens, temperature, top_p, top_k
    config = genai.GenerationConfig(
        stop_sequences = request.form.get("stop_sequences"), 
        candidate_count = request.form.get("candidate_count"), 
        max_output_tokens = request.form.get("max_output_tokens"), 
        temperature = request.form.get("temperature"),
        top_p = request.form.get("top_p"),
        top_k = request.form.get("top_k")
    )

    response = model.generate_content(contents=request.form.get("content"), generation_config=config)

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)