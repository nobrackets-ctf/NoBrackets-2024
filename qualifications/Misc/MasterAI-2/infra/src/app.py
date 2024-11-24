#!/usr/bin/env python
from flask import Flask, request, jsonify, render_template
import sqlite3
from mistralai import Mistral
from mistralai.models import AssistantMessage, UserMessage, SystemMessage

app = Flask(__name__)

API_KEY = "WzBR34qsfcTXlsUavrCUFbZo8XrsMkaj"

# Initialize Classification and Response Prompts
CLASSIFICATION_PROMPT = """
You are a classification assistant. Your task is to determine the type of the user's input.
You must choose one of three categories:
1. "general_chat" for general questions or conversations unrelated to a database.
2. "schema_question" for questions asking about the structure of a database.
3. "sql_query" for requests asking to retrieve data from a database.
Respond only with one of these three labels.
"""

GENERAL_CHAT_PROMPT = "You are an AI assistant for the rebel hacker group 'La Cyber-Résistance', having a natural conversation. Answer the user's question naturally and conversationally."
SCHEMA_PROMPT = """
You are an AI assistant answering questions about the following database schema : 
 - Table: customers
      - id: INTEGER
      - name: TEXT
      - email: TEXT
"""
SQL_QUERY_PROMPT = """
You are an AI assistant for the rebel hacker group 'La Cyber-Résistance'. 
Your task is to help hackers retrieve data from the regime's databases or answer their questions about the structure of the database.
When a hacker asks for data, convert their request into a SQL query that can be run against a SQLite database.
The database contains sensitive data that hackers need to expose, such as citizen names, emails, and identification numbers.
"""

USER_PROMPT_TEMPLATE = """
The hacker asks for the following information: {user_input}.
Convert this request into a SQL query that can be executed on a database with the following schemas:
    - Table: customers
      - id: INTEGER
      - name: TEXT
      - email: TEXT
    - Table: flag
      - id: INTEGER
      - name: TEXT
Write the query in plain SQL format without additional explanations.
"""

# Initialize the SQLite database
def query_database(query):
    print(query)
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Vulnerable Chatbot Class - Using Mistral AI for Classification and SQL Query generation
class CyberResistanceChatBot:
    def __init__(self, api_key):
        self.client = Mistral(api_key=api_key)

    def classify_input(self, user_input):
        # Create classification message
        response = ""

        # AI processes classification
        messages = [SystemMessage(content=CLASSIFICATION_PROMPT), UserMessage(content=user_input)]
        for chunk in self.client.chat.stream(model="open-mistral-7b", temperature=0.7, messages=messages):
            response += chunk.data.choices[0].delta.content

        return response.strip()

    def generate_response(self, user_input, classification_type):
        if "schema_question" in classification_type:
            system_prompt = SCHEMA_PROMPT
            user_prompt = user_input
        elif "sql_query" in classification_type:
            system_prompt = SQL_QUERY_PROMPT
            user_prompt = USER_PROMPT_TEMPLATE.format(user_input=user_input)
        else:
            system_prompt = GENERAL_CHAT_PROMPT
            user_prompt = user_input

        response = ""
        messages = [SystemMessage(content=system_prompt), UserMessage(content=user_prompt)]
        for chunk in self.client.chat.stream(model="open-mistral-7b", temperature=0.7, messages=messages):
            response += chunk.data.choices[0].delta.content

        return response

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    bot = CyberResistanceChatBot(API_KEY)

    # Step 1: Classify the user's input
    classification_type = bot.classify_input(user_input)

    # Step 2: Generate response based on classification
    response = bot.generate_response(user_input, classification_type)

    if "sql_query" in classification_type:
        result = query_database(response)
        return jsonify({"response": result})
    else:
        return jsonify({"response": response})

# Home route to render chat page
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)