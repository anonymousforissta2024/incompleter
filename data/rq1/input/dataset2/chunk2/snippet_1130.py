#Source: https://stackoverflow.com/questions/75900017/attributeerror-list-object-has-no-attribute-lower-in-sklearn
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

conversations = [   'Hello',   'Hi there!',   'How are you?',   'I am doing well.',   'That is good to hear.',   'Thank you',   'You are welcome.',   'What is your name?',   'My name is ChatBot.',   'Who created you?',   'I was created by OpenAI.']

def preprocess_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = text.split()
    return tokens

def generate_response(user_input, conversations):
   response = ''
   conversation_tokens = []
   conversation_tokens.append(preprocess_text(user_input))
   for conversation in conversations:
      conversation_tokens.append(preprocess_text(str(conversation)))
   tfidf_vectorizer = TfidfVectorizer(tokenizer=preprocess_text)
   tfidf_matrix = tfidf_vectorizer.fit_transform(conversation_tokens)
   similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
   idx = similarity_scores.argsort()[0][-2]
   flat = similarity_scores.flatten()
   flat.sort()
   score = flat[-2]
   if score == 0:
      response = response + 'I apologize, I do not understand.'
   else:
      response = response + conversations[idx]
   return response

while True:
   user_input = input('You: ')
   response = generate_response(user_input, conversations)
   print('ChatBot:', response)