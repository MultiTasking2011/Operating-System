from nltk import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.tokenize import word_tokenize
import nltk
import random
import ssl

training_data = [
    ("hello", "greeting"),
    ("hi there", "greeting"),
    ("how are you", "question"),
    ("what is your name", "question"),
    ("bye", "farewell"),
    ("see you later", "farewell"),
    ("thank you", "thanks"),
    ("thanks a lot", "thanks"),
]

def extract_features(text):
    words = word_tokenize(text.lower())
    return {word: True for word in words} 

try:
    _create_unverified_https_context = ssl._create_unverified_context
    ssl._create_default_https_context = _create_unverified_https_context
except AttributeError:
    pass

nltk.download('punkt')

# Prepare training data
training_set = [(extract_features(text), label) for text, label in training_data]

# Train the Naive Bayes Classifier
classifier = NaiveBayesClassifier.train(training_set)

# Test the chatbot with new inputs
def chatbot_response(user_input):
    features = extract_features(user_input)
    intent = classifier.classify(features)
    
    # Define responses for each intent
    responses = {
        "greeting": "Hello! How can I help you?",
        "question": "I'm here to answer your questions!",
        "question": "I'm good, i think",
        "farewell": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
    }
    return responses.get(intent, "I'm sorry, I didn't understand that.")

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot_response(user_input))
