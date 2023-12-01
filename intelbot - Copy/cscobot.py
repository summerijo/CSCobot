import json
import pickle
import random
import numpy as np
import psycopg2  # Import psycopg2 for PostgreSQL connection
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# Your existing code...
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.keras')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    # res = model.predict(np.array([bow]))[0]
    res = model.predict(np.array([bow]), verbose=0)[0]

    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="university",
    user="postgres",
    password="Password123"
)

# Other existing code...

def get_response(intents_list, intents_json, student_id):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    
    # Check if it's a personal query based on the intent tag or keywords
    personal_queries = ["name","dept_name", "tot_cred"]
    
    if tag in personal_queries:
        # Fetch user-specific data from the database
        cursor = conn.cursor()
        cursor.execute(f"SELECT {tag} FROM student WHERE id='{student_id}'")
        student_data = cursor.fetchone()
        cursor.close()
        
        # Process the personal query and generate a response
        if student_data:
            response = student_data[0] if student_data[0] else "I couldn't retrieve that information."
        else:
            response = "I couldn't retrieve your information."
    else:
        # Process non-personal queries
        for intent in list_of_intents:
            if intent['tag'] == tag:
                result = random.choice(intent['responses'])
                response = result
                break
        else:
            response = "I'm sorry, I couldn't understand your query."
    
    return response

print('CSCobot is running!')

while True:
    # Here, user_id should be obtained after the user logs in
    student_id = '12345'
    
    message = input("You: ")
    # Predict intent
    ints = predict_class(message)
    # Get response
    res = get_response(ints, intents, student_id)
    print("CSCobot:", res)