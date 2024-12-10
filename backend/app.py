
# Backend for AI-Driven Emergency Response System

from flask import Flask, request, jsonify

app = Flask(__name__)

# Example endpoint for crash detection data
@app.route('/crash-detection', methods=['POST'])
def crash_detection():
    data = request.json
    # Process the crash data
    return jsonify({"status": "success", "message": "Crash detected", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
