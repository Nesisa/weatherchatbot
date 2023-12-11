
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement

import sqlite3

def setup_database():
    # Connect to SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create table for chatbot data if not exists
    cursor.execute('CREATE TABLE IF NOT EXISTS chatbot_data (user_input TEXT, response TEXT)')

    # Check if data exists in the table
    existing_data = cursor.execute('SELECT * FROM chatbot_data').fetchall()

    # If no data exists, train the chatbot
    if not existing_data:
        train_chatbot()

    # Commit changes and close connection
    conn.commit()
    conn.close()

def train_chatbot():
    chatbot = ChatBot('WeatherBot')
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Use English language for training
    trainer.train('chatterbot.corpus.english')

    # Custom training data
    trainer = ListTrainer(chatbot)
    trainer.train([
        'What is the weather like in Corfe Castle?',
        'The weather in Corfe Castle is...'
        # Add more training data
    ])

    # Store training data in SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    for statement in chatbot.storage.filter():
        cursor.execute('INSERT INTO chatbot_data (user_input, response) VALUES (?, ?)',
                       (statement.text, statement.in_response_to))
    conn.commit()
    conn.close()

def get_response_from_chatbot(user_query):
    # Connect to SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Retrieve response from the database based on user query
    cursor.execute('SELECT response FROM chatbot_data WHERE user_input = ?', (user_query,))
    response = cursor.fetchone()

    # If a response is found, return it, otherwise use the chatbot
    if response:
        return response[0]
    else:
        # Create a ChatBot instance and get a response
        chatbot = ChatBot('WeatherBot')
        chatbot.storage.drop()
        train_chatbot()
        response = chatbot.get_response(user_query)
        return str(response)

    # Close the database connection
    conn.close()

# Example usage
user_query = "What is the weather like in Corfe Castle?"
response = get_response_from_chatbot(user_query)
print(response)
