import os
import openai
import gradio as gr
from flask import Flask

app = Flask(__name__)

# Set up OpenAI API key (use environment variables in Render)
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

# Gradio UI
gradio_interface = gr.Interface(fn=chat_with_gpt, inputs="text", outputs="text", title="AI Chatbot")

@app.route('/')
def home():
    return gradio_interface.launch(server_name="0.0.0.0", server_port=8080, share=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
