# Flask Email Server

This Flask application provides an API endpoint for sending emails using multiple SMTP servers with rate limiting and session management.

Client for this: [github.com/botsarefuture/email_delivery_client](https://github.com/botsarefuture/email_delivery_client)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/botsarefuture/email_delivery_service.git
    ```

2. Navigate to the directory:

    ```bash
    cd email_delivery_service
    ```

3. Install the required dependencies:

    ```bash
    pip install Flask
    ```

## Usage

1. Run the Flask server:

    ```bash
    python app.py
    ```

2. Send a POST request to the `/send_email` endpoint with the required parameters:

    - `email_from`: Sender's email address.
    - `email_to`: Recipient's email address.
    - `subject`: Email subject.
    - `text` (optional): Plain text content of the email.
    - `html` (optional): HTML content of the email.
    - `email` (optional): Sender's email address (if not provided in session).
    - `password` (optional): Sender's email password (if not provided in session).
    - `smtp_index` (optional): Index of the SMTP server to use (if not using default configuration).

Example usage with cURL:

```bash
curl -X POST http://localhost:5000/send_email \
    -H "Content-Type: application/json" \
    -d '{
        "email_from": "sender@example.com",
        "email_to": "recipient@example.com",
        "subject": "Test Email",
        "text": "This is a test email.",
        "email": "sender@example.com",
        "password": "password",
        "smtp_index": 0
    }'
```

## API Specification

### `POST /send_email`

Sends an email with the provided parameters.

#### Request Body

- `email_from`: Sender's email address.
- `email_to`: Recipient's email address.
- `subject`: Email subject.
- `text` (optional): Plain text content of the email.
- `html` (optional): HTML content of the email.
- `email` (optional): Sender's email address (if not provided in session).
- `password` (optional): Sender's email password (if not provided in session).
- `smtp_index` (optional): Index of the SMTP server to use (if not using default configuration).

#### Response

- Success (200 OK):

    ```json
    {
        "message": "Email sent successfully"
    }
    ```

- Error (4xx or 5xx):

    ```json
    {
        "error": "Error message"
    }
    ```

## Notes

- The server uses rate limiting to send one email every 2 seconds from each server.
- Multiple SMTP servers can be configured in the `smtp_servers` list.
- Session management is used to store default email configurations.
