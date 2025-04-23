# Groq-Based-Voice-Assistant

A Python-based voice assistant that uses speech recognition, text-to-speech, and the Groq API (with Llama 3) for natural language understanding.  
It can perform actions like opening applications, websites, and executing system commands.

---

## Features

- Voice input and speech output  
- Context-aware conversations using Groq's Llama 3 model  
- Action execution:
  - Open applications (Calculator, Chrome, Word, etc.)
  - Open websites (YouTube, Google, etc.)
  - System commands (lock, shutdown, restart)
  - Open special folders (Music, Videos, Documents)  
- Conversation memory for contextual understanding

---

## Prerequisites

- Python 3.8+  
- Windows OS (Linux/macOS support possible with modifications)  
- Microphone  
- Groq API key (free tier available)

---

## Installation

**1. Clone the repository**

   Run the following commands in your terminal:
   ```bash
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant
   ```

**2. Create and activate a virtual environment (recommended):**
  ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
  ```
3. **Install dependencies:**
  - pip install -r requirements.txt

  Set up your environment variables:
  - Rename .env.example to .env

  **Add your Groq API key:**
   - GROQ_API_KEY=your_api_key_here
   - PORCUPINE_ACCESS_KEY=your_access_key

## Project Structure

- `main.py`               – Main application logic  
- `voice_actions.py`      – Action execution handlers  
- `groq_response.py`      – Groq API interface  
- `requirements.txt`      – Python dependencies  
- `.env`                  – Environment variables (ignored by git)  
- `.env.example`          – Example environment file  
- `README.md`             – This file

---

## API Key Security

- Never commit your `.env` file to version control.
- Ensure `.gitignore` excludes `.env` (default behavior).
- Keep your Groq API key secure.

---

## Windows Focus

- Application paths are currently Windows-specific.
- For Linux/macOS, update `voice_actions.py` accordingly.

---

## Speech Recognition

- Requires an active internet connection (uses Google's speech recognition).
- For offline use, consider alternatives like `pocketsphinx`.

---

## Customization

To add more applications or commands:
1. Edit the `app_normalizations` dictionary in `voice_actions.py`.
2. Add new entries to the `apps` dictionary with the correct paths.
3. Update the system prompt in `groq_response.py` to recognize new commands.

---

## Troubleshooting

**Problem:** Speech recognition isn't working  
**Solution:** Check your microphone permissions and internet connection.

**Problem:** "Failed to open app" errors  
**Solution:** Verify application paths in `voice_actions.py` match your system.

**Problem:** API errors  
**Solution:** Verify your Groq API key is correct and has available quota.

---

## Video of Working:

[![ Demonstration video ](https://youtu.be/atKrsi1nr5M)]
