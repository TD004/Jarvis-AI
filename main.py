from wake_word import wait_for_wake_word
from speech_input import listen
from nlp_transformer import predict_intent
from actions import perform_action
from tts import speak
from memory import add_to_memory

CONFIDENCE_THRESHOLD = 0.60

speak("Jarvis online")

while True:
    wait_for_wake_word()
    speak("Yes?")

    text = listen()
    if not text:
        speak("I didn't catch that")
        continue

    intent, confidence = predict_intent(text)
    add_to_memory(text, intent)

    if confidence < CONFIDENCE_THRESHOLD:
        speak("I am not sure. Please repeat.")
        continue

    perform_action(intent)
