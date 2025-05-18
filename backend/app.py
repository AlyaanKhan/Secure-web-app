from flask import Flask, request, jsonify
from flask_cors import CORS
from cryptography.fernet import Fernet

app = Flask(__name__)
CORS(app)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({"error": "No message provided"}), 400

    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode()).decode()

    return jsonify({
        "encrypted": encrypted,
        "key": key.decode()
    })

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    encrypted = data.get('encrypted')
    key = data.get('key')
    password = data.get('password')

    if not encrypted or not key or not password:
        return jsonify({"error": "Missing encrypted message, key, or password"}), 400

    # Hardcoded password for authentication
    if password != 'letmein':
        return jsonify({"error": "Authentication failed: Incorrect password"}), 401

    try:
        fernet = Fernet(key.encode())
        decrypted = fernet.decrypt(encrypted.encode()).decode()
        return jsonify({"decrypted": decrypted})
    except Exception:
        return jsonify({"error": "Decryption failed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
