# voice_assistant.py
import webbrowser, datetime, pyttsx3, speech_recognition as sr, wikipediaapi

engine = pyttsx3.init()
def speak(text):
    engine.say(text); engine.runAndWait()

def open_google(): webbrowser.open("https://www.google.com")
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p"), now.strftime("%B %d, %Y")

# ... paste the rest of your assistant code here ...
if __name__ == "__main__":
    speak("Voice assistant started.")
