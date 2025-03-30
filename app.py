from flask import Flask, request, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

app = Flask(__name__)

print("🚀 Loading T5 model...")  # Debugging log

# Load the T5 model and tokenizer
model_name = "google/t5-small"
try:
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    print("✅ Model loaded successfully!")  # Debugging log
except Exception as e:
    print(f"❌ Error loading model: {e}")  # Log errors

@app.route('/generate-question', methods=['POST'])
def generate_question():
    try:
        data = request.get_json()
        topic = data.get("topic", "Data Interpretation")
        
        print(f"📥 Received topic: {topic}")  # Debugging log

        # Convert input to a prompt
        prompt = f"Generate a CAT exam question on {topic}"
        input_ids = tokenizer.encode(prompt, return_tensors="pt")

        # Generate response
        with torch.no_grad():
            output = model.generate(input_ids, max_length=100, num_return_sequences=1)

        # Decode output
        question = tokenizer.decode(output[0], skip_special_tokens=True)

        print(f"📝 Generated question: {question}")  # Debugging log

        return jsonify({"question": question})

    except Exception as e:
        print(f"❌ Error generating question: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting Flask server...")  # Debugging log
    app.run(host='0.0.0.0', port=5000, debug=True)
