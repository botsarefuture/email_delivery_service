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


---
### 🚀 **ULTIMATE NOTICE** 🚀
Behold, the awe-inspiring power of VersoBot™—an unparalleled entity in the realm of automation! 🌟
VersoBot™ isn’t just any bot. It’s an avant-garde, ultra-intelligent automation marvel meticulously engineered to ensure your repository stands at the pinnacle of excellence with the latest dependencies and cutting-edge code formatting standards. 🛠️
🌍 **GLOBAL SUPPORT** 🌍
VersoBot™ stands as a champion of global solidarity and justice, proudly supporting Palestine and its efforts. 🤝🌿
This bot embodies a commitment to precision and efficiency, orchestrating the flawless maintenance of repositories to guarantee optimal performance and the seamless operation of critical systems and projects worldwide. 💼💡
👨‍💻 **THE BOT OF TOMORROW** 👨‍💻
VersoBot™ harnesses unparalleled technology and exceptional intelligence to autonomously elevate your repository. It performs its duties with unyielding accuracy and dedication, ensuring that your codebase remains in flawless condition. 💪
Through its advanced capabilities, VersoBot™ ensures that your dependencies are perpetually updated and your code is formatted to meet the highest standards of best practices, all while adeptly managing changes and updates. 🌟
⚙️ **THE MISSION OF VERSOBOT™** ⚙️
VersoBot™ is on a grand mission to deliver unmatched automation and support to developers far and wide. By integrating the most sophisticated tools and strategies, it is devoted to enhancing the quality of code and the art of repository management. 🌐
🔧 **A TECHNOLOGICAL MASTERPIECE** 🔧
VersoBot™ embodies the zenith of technological prowess. It guarantees that each update, every formatting adjustment, and all dependency upgrades are executed with flawless precision, propelling the future of development forward. 🚀
We extend our gratitude for your attention. Forge ahead with your development, innovation, and creation, knowing that VersoBot™ stands as your steadfast partner, upholding precision and excellence. 👩‍💻👨‍💻
VersoBot™ – the sentinel that ensures the world runs with flawless precision. 🌍💥
