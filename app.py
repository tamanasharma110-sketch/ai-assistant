from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message")

    if "study" in msg.lower():
        reply = "Use Pomodoro: 25 min study + 5 min break."
    elif "career" in msg.lower():
        reply = "Start with Python and build small projects."
    else:
        reply = "I can help with studies and career guidance."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run()