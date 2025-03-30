from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the T5-based model for question generation
question_generator = pipeline("text2text-generation", model="ramsrigouthamg/t5_squad_v1")

@app.route("/generate-question", methods=["POST"])
def generate_question():
    data = request.json
    topic = data.get("topic", "")
    
    if not topic:
        return jsonify({"error": "Please provide a topic."}), 400
    
    prompt = f"Generate a CAT-level question based on the topic: {topic}"
    
    generated_question = question_generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    
    return jsonify({"topic": topic, "question": generated_question})

if __name__ == "__main__":
    app.run(debug=True)
