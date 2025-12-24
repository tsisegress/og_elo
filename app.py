from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    return jsonify({"answer": "mai nahi bta raha chat gpt krle"})

app.run(debug=True)
