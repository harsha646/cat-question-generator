from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "CAT Question Generator API is running!"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's dynamic port or default to 10000
    app.run(host="0.0.0.0", port=port)



