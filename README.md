# Microsoft Graph API with Python (App-Only Authentication)

This project demonstrates how to authenticate to **Microsoft Graph** using **app-only authentication** in Python and perform basic Microsoft Graph API operations.

The application uses **Microsoft Entra ID (Azure AD)** together with the **Microsoft Graph Python SDK** to securely authenticate without requiring user interaction. It was developed as part of my learning journey to understand cloud authentication, REST APIs, and secure application development.

---

## Project Overview

The application authenticates using a registered Microsoft Entra application and a client secret before making requests to Microsoft Graph.

Current functionality includes:

- Authenticate using **ClientSecretCredential**
- Obtain an OAuth access token
- List users within a Microsoft 365 tenant
- Retrieve organisation information
- Simple command-line menu interface

---

## Technologies Used

- Python 3
- Microsoft Graph SDK for Python
- Azure Identity
- Microsoft Entra ID (Azure AD)
- Microsoft Graph API

---

## Project Structure

```
.
├── main.py
├── graph.py
├── config.example.cfg
├── requirements.txt
├── .gitignore
└── README.md
```

> **Note:** `config.cfg` is excluded from source control and should never be committed.

---

## Configuration

Create a file named `config.cfg` in the project root.

```ini
[azure]
clientId = YOUR_CLIENT_ID
clientSecret = YOUR_CLIENT_SECRET
tenantId = YOUR_TENANT_ID
```

The application reads these credentials to authenticate against Microsoft Entra ID.

---

## Running the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

The application displays a simple interactive menu where you can:

- Display an access token
- List users
- Retrieve organisation details

---

## Skills Demonstrated

This project helped me develop practical experience with:

- OAuth 2.0 authentication
- Microsoft Entra ID application registration
- Microsoft Graph API
- Python SDK integration
- Secure credential management
- Configuration management using `.gitignore`
- Working with cloud APIs

---

## Security

Sensitive configuration files are intentionally excluded from GitHub.

Example `.gitignore`:

```gitignore
config.cfg
config.dev.cfg
venv/
__pycache__/
.env
```

Never commit:

- Client IDs
- Client Secrets
- Tenant IDs
- Access Tokens

---

## Learning Outcome

This project improved my understanding of how enterprise applications securely authenticate with Microsoft Graph using app-only permissions. It also gave me practical experience working with cloud APIs, access tokens, configuration management, and Microsoft's identity platform.

---

## Reference

This project was developed by following and extending the official Microsoft Learn tutorial:

https://learn.microsoft.com/en-us/graph/tutorials/python-app-only

---

## License

This repository is intended for educational and portfolio purposes.