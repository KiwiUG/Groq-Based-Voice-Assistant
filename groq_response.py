# groq_response.py
import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_groq_response(prompt, memory=[]):
    system_prompt = {
        "role": "system",
        "content": """You are a helpful voice assistant that only responds with JSON.
Your responses should contain these fields:
- action_type: one of [open_app, open_url, none]
- action_data: the name of the app or url, or empty string if none
- reply: a short phrase to read aloud to the user

Examples:
User: open calculator
Assistant:
{
  "action_type": "open_app",
  "action_data": "calc",
  "reply": "Opening Calculator."
}

User: what's the time
Assistant:
{
  "action_type": "none",
  "action_data": "",
  "reply": "It's 3:45 PM."
}
"""
    }

    memory = [system_prompt] + memory
    memory.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=memory
    )

    raw_reply = response.choices[0].message.content

    try:
        response_json = json.loads(raw_reply)
    except json.JSONDecodeError:
        response_json = {
            "action_type": "none",
            "action_data": "",
            "reply": "Sorry, I didn't understand that."
        }

    return response_json, memory
#end