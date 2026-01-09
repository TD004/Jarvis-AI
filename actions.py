import os
from datetime import datetime
from tts import speak
from memory import get_last_intent, clear_memory

def perform_action(intent):
    last_intent = get_last_intent()

    if intent != last_intent and last_intent is not None:
        speak("Okay, correcting")

    if intent == "open_browser":
        speak("Opening browser")
        os.system("start chrome")

    elif intent == "get_time":
        time = datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif intent == "play_music":
        speak("Playing music")

    elif intent == "shutdown":
        speak("Shutting down system")
        clear_memory()
        # os.system("shutdown /s /t 5")

    else:
        speak("I cannot do that yet")
