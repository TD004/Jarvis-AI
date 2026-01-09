import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.optim import AdamW

sentences = [
    "open chrome",
    "start browser",
    "launch chrome",
    "what time is it",
    "tell me the time",
    "play music",
    "start music",
    "shutdown computer",
    "turn off system"
]

labels = [0,0,0,1,1,2,2,3,3]

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
encodings = tokenizer(sentences, truncation=True, padding=True, return_tensors="pt")

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=4
)

optimizer = AdamW(model.parameters(), lr=5e-5)
label_tensor = torch.tensor(labels)

model.train()
for epoch in range(10):
    outputs = model(**encodings, labels=label_tensor)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    print(f"Epoch {epoch} | Loss: {loss.item()}")

torch.save(model.state_dict(), "jarvis_model.pt")
print("✅ Model saved as jarvis_model.pt")
