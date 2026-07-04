import configparser
from flask import Flask, request, redirect
from msal import ConfidentialClientApplication

# Load secrets from config.cfg
config = configparser.ConfigParser()
config.read("config.cfg")

CLIENT_ID = config["azure"]["clientId"]
CLIENT_SECRET = config["azure"]["clientSecret"]
TENANT_ID = config["azure"]["tenantId"]

REDIRECT_URI = "http://localhost:5000/auth"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["User.Read"]

app = Flask(__name__)

@app.route("/")
def home():
    cca = ConfidentialClientApplication(
        CLIENT_ID,
        CLIENT_SECRET,
        authority=AUTHORITY
    )
    auth_url = cca.get_authorization_request_url(
        SCOPE,
        redirect_uri=REDIRECT_URI
    )
    return redirect(auth_url)

@app.route("/auth")
def auth():
    code = request.args.get("code")
    cca = ConfidentialClientApplication(
        CLIENT_ID,
        CLIENT_SECRET,
        authority=AUTHORITY
    )
    result = cca.acquire_token_by_authorization_code(
        code,
        scopes=SCOPE,
        redirect_uri=REDIRECT_URI
    )
    return f"Access Token: {result['access_token']}"

app.run(port=5000)
