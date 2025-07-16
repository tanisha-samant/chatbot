import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

# Fix resource loading
nltk.data.path.append("/home/codespace/nltk_data")
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json") as file:
    data = json.load(file)

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def lemmatize(words):
    return [lemmatizer.lemmatize(w.lower()) for w in words]

def match_intent(sentence):
    sentence_words = lemmatize(tokenize(sentence))
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = lemmatize(tokenize(pattern))
            if set(pattern_words).intersection(set(sentence_words)):
                return random.choice(intent["responses"])
    return random.choice(data["intents"][-1]["responses"])
