from flask import Flask, request, jsonify
import boto3
import os
from datetime import datetime

app = Flask(__name__)

# Health check route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend is running!"})

# Example prediction route (adjust to your ML logic)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    # Dummy example: just echo the input
    return jsonify({"input_received": data})

# 🔹 Test S3 upload route
@app.route("/test-s3-upload", methods=["GET"])
def test_s3_upload():
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name="us-east-1"  # Change if your bucket is in a different region
        )

        file_content = f"Test upload at {datetime.utcnow()}"
        file_name = f"test_upload_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.txt"

        s3.put_object(
            Bucket="generative-ai-media",
            Key=file_name,
            Body=file_content
        )

        return jsonify({"success": True, "message": f"Uploaded {file_name} to S3"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
