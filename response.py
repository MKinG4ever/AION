import json
import random
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

# Prepare training data
patterns = []
labels = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        labels.append(intent['intent'])

# Vectorize patterns
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

# Train classifier
classifier = LogisticRegression()
classifier.fit(X, labels)


def classify_intent(text: str):
    """
    Classify the intent of the input text using a trained model.

    :param text: The input text to classify.
    :return: Classified intent.
    """
    X_test = vectorizer.transform([text])
    prediction = classifier.predict(X_test)
    return prediction[0]


def generate_response(intent: str):
    """
    Generate a response based on the classified intent using predefined responses.

    :param intent: The classified intent.
    :return: Generated response.
    """
    for i in intents['intents']:
        if i['intent'] == intent:
            return random.choice(i['responses'])


# Example usage
if __name__ == "__main__":
    user_input = "Can you help me?"
    intent = classify_intent(user_input)
    response = generate_response(intent)
    print(f"Bot: {response}")
