import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from memory import get_context

intents = {
    0: "open_browser",
    1: "get_time",
    2: "play_music",
    3: "shutdown"
}

tokenizer = DistilBertTokenizer.from_pretrained(
    "distilbert-base-uncased"
)

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=len(intents)
)

model.load_state_dict(
    torch.load("jarvis_model.pt", map_location=torch.device("cpu"))
)
model.eval()

def predict_intent(text):
    context = get_context()
    combined = f"{context} {text}".strip()

    inputs = tokenizer(
        combined,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)
    confidence, predicted_class = torch.max(probs, dim=1)

    return intents[predicted_class.item()], confidence.item()
