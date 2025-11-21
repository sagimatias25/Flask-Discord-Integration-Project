# Flask-Discord-Integration-Project

A Flask web application with three endpoints to facilitate the submission, transmission, and retrieval of messages to/from a Discord server and stored in a SQLite3 database.

## 🎯 Project Overview

This project implements a seamless integration between a Flask web application and Discord, allowing users to:
- Submit text messages through a web interface
- Transmit messages to a specified Discord server in real-time
- Retrieve and display recent messages (last 30 minutes) from the database
- Store all messages in a persistent SQLite3 database

## 📋 Table of Contents

- [Features](#features)
- [Mission Objectives](#mission-objectives)
- [Endpoints](#endpoints)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Security Considerations](#security-considerations)
- [License](#license)

## ✨ Features

✅ **Web Interface**: User-friendly form for submitting messages
✅ **Real-time Discord Integration**: Messages sent immediately to Discord server
✅ **Database Storage**: SQLite3 database for persistent message storage
✅ **Message Retrieval**: View recent messages with timestamps
✅ **Input Validation**: Comprehensive validation and error handling
✅ **Flash Messages**: User feedback for successful/failed operations
✅ **Responsive Design**: Clean HTML interface

## 🎓 Mission Objectives

### Endpoint 1 - Input Text
**Description**: This endpoint receives text input from users through a POST request. Users can submit their messages, and any text content submitted through this endpoint will be processed for further transmission.

**Implementation**:
- Accepts POST requests with text data
- Validates input data
- Sends validated text to the next endpoint for processing

### Endpoint 2 - Discord Integration
**Description**: The text received from Endpoint 1 will be transmitted to a specified Discord server for real-time communication. This involves setting up a Discord bot, configuring authentication, and sending the text as a message to a predefined channel on the server.

**Implementation**:
- Uses discord.py library to establish connection with Discord server
- Flask app acts as a bridge between user input and Discord server
- Forwards text content securely

### Endpoint 3 - Message Retrieval
**Description**: This endpoint will display all the messages that have been submitted and sent to the Discord server in the last 30 minutes. It provides users with a real-time snapshot of recent conversations.

**Implementation**:
- Queries the SQLite3 database
- Retrieves messages recorded in the last 30 minutes
- Displays results in a structured format as a response

## 🔌 Endpoints

### 1. `/` - Main Form (GET)
```
Route: GET /
Description: Displays the main web form for message submission
Response: HTML form with message textarea and submit button
```

### 2. `/input_text` - Submit Message (POST)
```
Route: POST /input_text
Description: Receives text input, sends to Discord, and stores in database
Request Body: 
  - text (string): The message content
Response: 
  - Success: Redirect to main page with success message
  - Error: Returns 400 Bad Request if text is empty
```

### 3. `/messages` - Retrieve Messages (GET)
```
Route: GET /messages
Description: Displays all messages from the last 30 minutes
Response: HTML page with formatted list of recent messages and timestamps
```

## 💻 Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/sagimatias25/Flask-Discord-Integration-Project.git
cd Flask-Discord-Integration-Project
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install flask requests
```

## ⚙️ Configuration

### Discord Webhook Setup

1. **Create a Discord Server** (if you don't have one)
2. **Create a Channel** where messages will be sent
3. **Get Webhook URL**:
   - Right-click on the channel → Integrations → Webhooks
   - Click "New Webhook"
   - Copy the webhook URL

4. **Update the code**:
   - Replace `DISCORD_WEBHOOK_URL` in `app.py` with your webhook URL

```python
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN'
```

### Database Configuration

The application uses SQLite3 which requires no additional configuration. The database file (`messages.db`) will be created automatically on first run.

## 🚀 Usage

1. **Start the Flask application**
```bash
python app.py
```

2. **Access the web interface**
Open your browser and navigate to:
```
http://localhost:5000/
```

3. **Submit a message**
   - Type your message in the textarea
   - Click "Send"
   - You'll see a success message
   - The message appears in Discord immediately

4. **View recent messages**
   - Click "View Recent Messages" link on the main page
   - Or navigate to: `http://localhost:5000/messages`
   - See all messages from the last 30 minutes with timestamps

## 📁 Project Structure

```
Flask-Discord-Integration-Project/
│
├── app.py                 # Main Flask application
├── messages.db            # SQLite3 database (created automatically)
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
```

### app.py - Main Application File

```python
import requests
import sqlite3
from flask import Flask, request, flash, url_for, render_template_string
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = 'secret'

# Database initialization
def init_db():
    # Creates messages table with id, content, and timestamp

# Discord integration
def send_to_discord(text):
    # Sends message to Discord webhook

# Main endpoints
@app.route('/')                      # Main form
@app.route('/input_text', methods=['POST'])  # Submit message
@app.route('/messages', methods=['GET'])     # View recent messages
```

## 🔐 Security Considerations

⚠️ **Important Security Notes**:

1. **Secret Key**: Change the `secret_key` from 'secret' to a strong random value
   ```python
   app.secret_key = 'your-secure-random-key'
   ```

2. **Webhook URL Protection**: 
   - Never commit webhook URLs to version control
   - Use environment variables for sensitive data
   ```python
   import os
   DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
   ```

3. **Input Validation**:
   - The application validates that text input is not empty
   - Consider adding length limits and sanitization for production

4. **Debug Mode**:
   - Disable debug mode (`debug=False`) in production
   ```python
   if __name__ == '__main__':
       init_db()
       app.run(debug=False)  # Production setting
   ```

5. **Database Security**:
   - Use proper access controls for messages.db
   - Consider encrypting sensitive data

## 📦 Dependencies

- **Flask**: Web framework for Python
- **Requests**: HTTP library for sending webhook requests
- **sqlite3**: Built-in Python database library
- **werkzeug**: Utility library for routing

## 🛡️ Copyright & Protection

**This project is public but protected against unauthorized copying or use.**

All code, documentation, and associated materials are the intellectual property of the author. While the repository is publicly accessible, any reproduction, modification, or distribution of this code for commercial purposes without explicit permission is prohibited.

## 📝 License

This project is provided as-is for educational and authorized use only.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📧 Support

For issues, questions, or feedback, please open an issue on GitHub.

---

**Author**: Sagi Matias (sagimatias25)
**Created**: November 2025
**Status**: Active Development
