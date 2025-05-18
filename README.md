# Secure Message Encryption Web Application

A full-stack web application that provides secure message encryption and decryption capabilities using Fernet symmetric encryption.

## Features

- End-to-end message encryption
- Secure key management
- User authentication
- Modern, responsive UI
- RESTful API architecture

## Tech Stack

### Frontend
- React 19
- TypeScript
- Material-UI
- Axios for API calls
- React Router for navigation

### Backend
- Python Flask
- Flask-CORS
- Fernet encryption (cryptography)

## Setup Instructions

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

## API Endpoints

### POST /encrypt
Encrypts a message and returns the encrypted text and key.

### POST /decrypt
Decrypts a message using the provided key and password.

## Security Features
- Fernet symmetric encryption
- Password-based authentication
- Secure key management
- CORS protection

## Contributing
Feel free to submit issues and enhancement requests! 
