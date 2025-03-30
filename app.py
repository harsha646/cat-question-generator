from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "CAT Question Generator API is running!"

@app.route('/generate-question', methods=['GET'])
def generate_question():
    topic = request.args.get('topic', 'default')
    sample_question = {
        "question": f"What is an example question for {topic}?",
        "options": ["A", "B", "C", "D"],
        "answer": "A"
    }
    return jsonify(sample_question)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
