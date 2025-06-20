# Gemini Chat API – Backend for Proton Alexa Skill

This is a Flask-based backend application that integrates with **Google Gemini 2.0 Flash API** to support the **Proton Alexa Skill**. It enables real-time, session-based chat interactions per user using generative AI.

## 🌐 Deployed API Endpoint

**Base URL:** [`https://gemresponse.onrender.com`](https://gemresponse.onrender.com)

---

## ⚙️ Features

- 🔐 Gemini 2.0 Flash Model integration (via `google.generativeai`)
- 🧠 Per-user session management
- 💬 Chat endpoint for real-time messaging
- ❌ Session termination endpoint
- 🧼 Sanitized responses (special characters `@#$*` removed)

---

## 📦 Requirements

- Python 3.7+
- Flask
- Google Generative AI SDK (`google-generativeai`)

### Install dependencies:

```bash
pip install flask google-generativeai
```

---

## 🚀 Running Locally

```bash
python app.py
```

This runs the server on: `http://localhost:5000`

---

## 🔑 Google Gemini API Configuration

Replace the placeholder in the code with your actual API key:

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

## 📡 API Endpoints

### 1. **POST** `/gemini`

Initiates or continues a chat session with a given user.

#### Request:

```json
{
  "user_id": "user123",
  "query": "What is the capital of France?"
}
```

#### Response:

```json
{
  "response": "The capital of France is Paris."
}
```

---

### 2. **POST** `/end_session`

Ends a specific user session.

#### Request:

```json
{
  "user_id": "user123"
}
```

#### Response:

```json
{
  "message": "Session ended."
}
```

---

## 🧠 How It Works with Alexa Skill (Proton)

1. **Alexa Skill** captures user's spoken query.
2. The query is sent to the `/gemini` endpoint with a unique `user_id`.
3. The backend uses **Google Gemini 2.0 Flash** to generate a context-aware response.
4. The response is returned to Alexa and spoken back to the user.

---

## 📁 Project Structure

```bash
.
├── app.py             # Main Flask app
└── README.md          # API documentation (this file)
```

---


## 🧠 Credits

- Powered by: [Google Generative AI](https://ai.google.dev/)
- Deployed on: [Render](https://render.com/)
- Created for: **Proton Alexa Skill**
