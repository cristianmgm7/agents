#!/usr/bin/env python3
"""
Carbon Voice OAuth2 Helper
Helps obtain API key through OAuth2 flow with redirect URL handling
"""

import os
import webbrowser
import http.server
import socketserver
import urllib.parse
import urllib.request
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OAuth2 Configuration
CLIENT_ID = os.getenv('CARBON_VOICE_CLIENT_ID')
CLIENT_SECRET = os.getenv('CARBON_VOICE_CLIENT_SECRET')
REDIRECT_URI = os.getenv('CARBON_VOICE_REDIRECT_URI', 'http://localhost:3000/oauth/callback')
AUTHORIZATION_ENDPOINT = 'https://api.carbonvoice.app/oauth/authorize'  # Update with actual endpoint
TOKEN_ENDPOINT = 'https://api.carbonvoice.app/oauth/token'  # Update with actual endpoint

class OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
    """Handles OAuth2 callback"""

    def do_GET(self):
        """Handle the OAuth2 callback"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Parse the authorization code from the URL
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        if 'code' in query_params:
            authorization_code = query_params['code'][0]
            print(f"\n✅ Authorization code received: {authorization_code}")

            # Exchange code for access token
            access_token = self.exchange_code_for_token(authorization_code)

            if access_token:
                # Save to .env file
                self.save_token_to_env(access_token)

                self.wfile.write(b'<html><body><h1>Success!</h1><p>Your Carbon Voice API key has been saved to .env file.</p><p>You can close this window.</p></body></html>')
            else:
                self.wfile.write(b'<html><body><h1>Error</h1><p>Failed to exchange authorization code for access token.</p></body></html>')
        else:
            self.wfile.write(b'<html><body><h1>Error</h1><p>No authorization code received.</p></body></html>')

    def exchange_code_for_token(self, authorization_code):
        """Exchange authorization code for access token"""
        try:
            data = urllib.parse.urlencode({
                'grant_type': 'authorization_code',
                'code': authorization_code,
                'redirect_uri': REDIRECT_URI,
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET
            }).encode()

            req = urllib.request.Request(TOKEN_ENDPOINT, data=data, method='POST')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')

            with urllib.request.urlopen(req) as response:
                token_data = json.loads(response.read().decode())
                return token_data.get('access_token')

        except Exception as e:
            print(f"❌ Error exchanging code for token: {e}")
            return None

    def save_token_to_env(self, access_token):
        """Save the access token to .env file"""
        env_file = '.env'

        # Read existing .env file
        env_content = {}
        if os.path.exists(env_file):
            with open(env_file, 'r') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        env_content[key] = value

        # Update or add CARBON_VOICE_API_KEY
        env_content['CARBON_VOICE_API_KEY'] = access_token

        # Write back to .env file
        with open(env_file, 'w') as f:
            for key, value in env_content.items():
                f.write(f'{key}={value}\n')

        print(f"✅ API key saved to {env_file}")

def start_oauth_flow():
    """Start the OAuth2 authorization flow"""
    if not CLIENT_ID:
        print("❌ CARBON_VOICE_CLIENT_ID not found in .env")
        return

    # Build authorization URL
    auth_url = (
        f"{AUTHORIZATION_ENDPOINT}?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={urllib.parse.quote(REDIRECT_URI)}&"
        f"response_type=code&"
        f"scope=read,write"  # Adjust scopes as needed
    )

    print("🌐 Opening browser for OAuth2 authorization...")
    print(f"📱 If browser doesn't open, visit: {auth_url}")
    print("🔄 Waiting for authorization callback...")

    # Open browser
    webbrowser.open(auth_url)

    # Start local server to handle callback
    port = 3000
    with socketserver.TCPServer(("", port), OAuthCallbackHandler) as httpd:
        print(f"🚀 Local server listening on port {port}")
        print("🔄 Complete authorization in your browser...")
        httpd.serve_request()  # Handle one request then exit

if __name__ == "__main__":
    print("🚀 Carbon Voice OAuth2 Helper")
    print("=" * 40)

    if not CLIENT_ID or not CLIENT_SECRET:
        print("❌ Missing OAuth2 credentials in .env")
        print("   Required: CARBON_VOICE_CLIENT_ID, CARBON_VOICE_CLIENT_SECRET")
        exit(1)

    start_oauth_flow()
