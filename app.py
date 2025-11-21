import requests
import sqlite3
from flask import Flask, request, flash, url_for, render_template_string
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = 'secret'

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1440404139577315511/AMwgrlaLepiLZxCtGz4ljWvYFADS2jjxMcr1Zt6qEJ6eUwVdfIactQ9w2pOOYKH1A2Lz'


def init_db():
    connection = sqlite3.connect('messages.db')
    connection.execute('''CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY, 
        content TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    connection.commit()
    connection.close()


def send_to_discord(text):
    payload = {'content': text}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)


@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Send a Message to Discord</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <p>{{ message }}</p>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form action="/input_text" method="POST">
            <textarea name="text"></textarea>
            <button type="submit">Send</button>
        </form>
        <br>
        <a href="/messages">View Recent Messages</a>
    </body>
    </html>
    '''
    return render_template_string(html)


def save_message(text):
    connection = sqlite3.connect('messages.db')
    connection.execute('INSERT INTO messages (content) VALUES (?)', (text,))
    connection.commit()
    connection.close()


@app.route('/input_text', methods=['POST'])
def input_text():
    text = request.form.get('text')
    if not text:
        flash('No text provided', 'error')
        return 'No text provided', 400
    # send the request to discord server
    send_to_discord(text)
    save_message(text)
    flash('your message has been saved', 'success')
    return redirect(url_for('index'))


@app.route('/messages', methods=['GET'])
def get_messages():
    connection = sqlite3.connect('messages.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT content, timestamp 
        FROM messages 
        WHERE timestamp >= datetime('now', '-30 minutes')
        ORDER BY timestamp DESC
    ''')
    messages = cursor.fetchall()
    connection.close()

    html = '''
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Recent Messages (Last 30 Minutes)</h1>
        <ul>
    '''
    for msg in messages:
        html += f'<li>{msg[0]} - {msg[1]}</li>'

    html += '''
        </ul>
        <a href="/">Back to form</a>
    </body>
    </html>
    '''
    return render_template_string(html)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
