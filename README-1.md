# Study Assistant Chatbot 🤖

An LLM-powered chatbot built to help B.Tech Computer Science students understand concepts through simple explanations and code examples. Powered by Google's Gemini API.

## 🎯 Objective

Provide an accessible, conversational tool for students to ask academic/programming questions and get clear, example-driven answers — built and deployed entirely from a mobile device.

## 🛠️ Tools & Technologies

- **Python** — core language
- **Flask** — backend web framework
- **Google Gemini API** (`google-genai` SDK, `gemini-3.5-flash` model) — the LLM powering responses
- **HTML/CSS** — frontend chat interface
- **Gunicorn** — production WSGI server
- **Render** — deployment/hosting

## ⚙️ How It Works

1. User submits a message through the chat interface
2. Flask receives the message via a POST request
3. The message is sent to Gemini API using a persistent chat session (`client.chats.create()`), which maintains conversation context
4. A **system prompt** shapes the AI's behavior — keeping it focused on academic/programming help, with clear, concise, example-driven responses
5. The AI's response is returned and rendered back to the user

## 🔐 Security Practice

The Gemini API key is never hardcoded in the source code. It's read at runtime from an environment variable (`GEMINI_API_KEY`), set securely in Render's dashboard — keeping it safe even though the repository is public.

## 🚀 Live Demo

https://study-chatbot-25wu.onrender.com

*(Note: free-tier hosting may take a few seconds to wake up on first load.)*

## 📁 Project Structure

```
├── app.py                  # Flask backend + Gemini API integration
├── templates/
│   └── index.html          # Chat interface
├── requirements.txt        # Dependencies
```

## 🚀 How to Run Locally

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set your Gemini API key as an environment variable: `GEMINI_API_KEY`
4. Run: `python app.py`

## 🔑 Key Concepts Demonstrated

- REST API integration (Gemini API)
- Prompt engineering & system prompts
- Conversational context/memory handling
- Flask backend development (routes, request handling)
- Environment variable security practices
- End-to-end deployment (GitHub → Render)

## 👤 Author

Sarthak — B.Tech CSE (AI/ML), Adamas University
