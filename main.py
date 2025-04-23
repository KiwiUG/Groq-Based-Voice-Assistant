# main.py
import speech_recognition as sr
import pyttsx3
from groq_response import get_groq_response
from voice_actions import perform_action

# Initialize speech recognizer and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Optional: Set a slower speech rate for TTS
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Network error.")
    return ""

def main():
    memory = []
    speak("Hey, I'm ready. Just say something.")

    while True:
        query = listen()
        if not query:
            continue

        if "exit" in query or "stop" in query:
            speak("Goodbye!")
            break

        response_json, memory = get_groq_response(query, memory)
        speak(response_json["reply"])
        perform_action(response_json["action_type"], response_json["action_data"])

if __name__ == "__main__":
    main()
#end