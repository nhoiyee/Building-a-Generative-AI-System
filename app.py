from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask AI backend!"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Dummy example: echo input
    return jsonify({"input_received": data})

if __name__ == '__main__':
    # Use 0.0.0.0 so Docker container exposes it externally
    app.run(host='0.0.0.0', port=5000, debug=True)
