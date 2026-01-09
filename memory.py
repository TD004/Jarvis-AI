from collections import deque

conversation_memory = deque(maxlen=5)

def add_to_memory(text, intent=None):
    conversation_memory.append({
        "text": text,
        "intent": intent
    })

def get_context():
    return " ".join(item["text"] for item in conversation_memory)

def get_last_intent():
    if conversation_memory:
        return conversation_memory[-1]["intent"]
    return None

def clear_memory():
    conversation_memory.clear()
