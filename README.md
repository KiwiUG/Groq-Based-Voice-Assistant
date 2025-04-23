# Groq-Based-Voice-Assistant

A Python-based voice assistant that uses speech recognition, text-to-speech, and the Groq API (with Llama 3) for natural language understanding. Can perform actions like opening applications, websites, and system commands.

![Voice Assistant Demo](https://via.placeholder.com/800x400?text=Voice+Assistant+Demo) 
(Consider adding a screenshot or demo GIF here)

## Features

-  Voice input and speech output
-  Context-aware conversations using Groq's Llama 3 model
-  Action execution:
  - Open applications (Calculator, Chrome, Word, etc.)
  - Open websites (YouTube, Google, etc.)
  - System commands (lock, shutdown, restart)
  - Open special folders (Music, Videos, Documents)
- Conversation memory for contextual understanding

## Prerequisites

- Python 3.8+
- Windows OS (Linux/macOS support possible with modifications)
- Microphone
- Groq API key (free tier available)

## Installation

1. Clone the repository:
   ->bash
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant

Create and activate a virtual environment (recommended):
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Set up your environment variables:

Rename .env.example to .env

Add your Groq API key:
GROQ_API_KEY=your_api_key_here

voice-assistant/
├── main.py               # Main application logic
├── voice_actions.py      # Action execution handlers
├── groq_response.py      # Groq API interface
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (ignored by git)
├── .env.example          # Example environment file
└── README.md             # This file

Important Notes
API Key Security:

Never commit your .env file to version control
The .gitignore file should exclude .env by default
Your Groq API key is sensitive - keep it secure

Windows Focus:

Application paths are currently Windows-specific
Modify voice_actions.py for Linux/macOS support

Speech Recognition:

Requires an active internet connection for Google's speech recognition
For offline use, consider alternative recognizers like pocketsphinx

Customization
To add more applications or commands:
Edit the app_normalizations dictionary in voice_actions.py
Add new entries to the apps dictionary with the correct paths
Update the system prompt in groq_response.py to recognize new commands

Troubleshooting
Problem: Speech recognition isn't working
Solution: Check your microphone permissions and internet connection
Problem: "Failed to open app" errors
Solution: Verify application paths in voice_actions.py match your system
Problem: API errors
Solution: Verify your Groq API key is correct and has available quota
