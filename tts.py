import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("🤖 JARVIS:", text)
    engine.say(text)
    engine.runAndWait()
