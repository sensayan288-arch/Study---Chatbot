import os
from flask import Flask, request, render_template
from google import genai
from google.genai import types

app = Flask(__name__)

# API key is read from Render's environment variables, never hardcoded here
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

chat = client.chats.create(
    model='gemini-3.5-flash',
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a helpful study assistant for B.Tech Computer Science "
            "students. Explain concepts clearly with simple examples, prefer "
            "code snippets when relevant, and keep answers concise. If asked "
            "something unrelated to academics or programming, politely "
            "redirect back to studies."
        )
    )
)

@app.route('/', methods=['GET', 'POST'])
def home():
    reply = None
    user_message = None
    if request.method == 'POST':
        user_message = request.form['message']
        response = chat.send_message(user_message)
        reply = response.text
    return render_template('index.html', reply=reply, user_message=user_message)

if __name__ == '__main__':
    app.run(debug=True)
