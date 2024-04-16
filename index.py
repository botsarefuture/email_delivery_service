import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Define SMTP servers with their configurations
smtp_servers = [
    {"host": "smtp.example1.com", "port": 587},
    {"host": "smtp.example2.com", "port": 587},
    # Add more SMTP servers if needed
]

# Create SMTP connections
smtp_connections = [smtplib.SMTP(server['host'], server['port']) for server in smtp_servers]

# Create a dictionary to store default email configurations
default_configs = {}

# Rate limit function
def rate_limit():
    rate_limit.last_time = getattr(rate_limit, 'last_time', 0)
    elapsed = time.time() - rate_limit.last_time
    if elapsed < 2:
        time.sleep(2 - elapsed)
    rate_limit.last_time = time.time()

# Function to send email
def send_email(email_from, email_to, subject, text, html, server_index):
    smtp_connection = smtp_connections[server_index]

    message = MIMEMultipart("alternative")
    message["From"] = email_from
    message["To"] = email_to
    message["Subject"] = subject

    if text:
        part1 = MIMEText(text, "plain")
        message.attach(part1)
    if html:
        part2 = MIMEText(html, "html")
        message.attach(part2)

    rate_limit()

    try:
        smtp_connection.sendmail(email_from, email_to, message.as_string())
        return {"message": "Email sent successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500

# API endpoint to send email
@app.route('/send_email', methods=['POST'])
def send_email_api():
    data = request.json
    email_from = data.get('email_from')
    email_to = data.get('email_to')
    subject = data.get('subject')
    text = data.get('text')
    html = data.get('html')

    if not all([email_from, email_to, subject]):
        return jsonify({"error": "Missing required fields"}), 400

    if not text and not html:
        return jsonify({"error": "No email content provided"}), 400

    if 'email' in session and 'password' in session:
        email = session['email']
        password = session['password']
        server_index = default_configs.get(email)
        if server_index is None:
            return jsonify({"error": "Default email configuration not found"}), 400
    else:
        email = data.get('email')
        password = data.get('password')
        server_index = None

    if server_index is None:
        # If default configuration is not found or not using saved configuration,
        # prompt for SMTP server details
        smtp_index = data.get('smtp_index')
        if smtp_index is None:
            return jsonify({"error": "SMTP server index not provided"}), 400

        smtp_server = smtp_servers[smtp_index]
        smtp_host = smtp_server['host']
        smtp_port = smtp_server['port']

        smtp_connection = smtplib.SMTP(smtp_host, smtp_port)
        smtp_connection.starttls()

        try:
            smtp_connection.login(email, password)
        except smtplib.SMTPAuthenticationError:
            return jsonify({"error": "Invalid email address or password"}), 401

        smtp_connections.append(smtp_connection)

        server_index = len(smtp_connections) - 1

    session['email'] = email
    session['password'] = password
    default_configs[email] = server_index

    result, status_code = send_email(email_from, email_to, subject, text, html, server_index)

    # Cycle to the next server
    next_server_index = (server_index + 1) % len(smtp_connections)
    default_configs[email] = next_server_index

    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
