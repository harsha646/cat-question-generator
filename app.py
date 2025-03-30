from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "CAT Question Generator API is running!"

import os
port = int(os.environ.get("PORT", 10000))  # Default to 10000 if PORT is not set
app.run(host="0.0.0.0", port=port)





