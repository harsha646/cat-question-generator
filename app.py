from flask import Flask, request, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)

# Load the T5 model and tokenizer
model_name = "google/t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

@app.route('/generate-question', methods=['POST'])
def generate_question():
    data = request.get_json()
    topic = data.get("topic", "Data Interpretation")
    
    # Convert input to a prompt
    prompt = f"Generate a CAT exam question on {topic}"

    # Encode input
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate response
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)

    # Decode output
    question = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({"question": question})

if __name__ == '__main__':
    app.run(debug=True)
