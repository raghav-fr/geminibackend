import re
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="AIzaSyDC2603M6IyhlYlGirpom8DpDFSlzyw5Hk")

# Store chat sessions per user
sessions = {}

def get_chat(user_id):
    if user_id not in sessions:
        chat = genai.GenerativeModel("gemini-2.0-flash").start_chat()
        sessions[user_id] = chat
    return sessions[user_id]

@app.route('/gemini', methods=['POST'])
def gemini_handler():
    data = request.get_json()

    user_id = data.get("user_id")
    user_query = data.get("query")

    if not user_id or not user_query:
        return jsonify({"error": "Missing user_id or query"}), 400

    try:
        chat = get_chat(user_id)
        response = chat.send_message(user_query)
        result = re.sub(r"[@#$*]", "", response.text)
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/end_session', methods=['POST'])
def end_session():
    data = request.get_json()
    user_id = data.get("user_id")
    if user_id in sessions:
        sessions.pop(user_id)
    return jsonify({"message": "Session ended."})

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port = 5000 , debug=True)
