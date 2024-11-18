#!/usr/bin/env python3

import sys
import requests

# Explicit "allow" list
ALLOWED_USERS = ["fuomag9","root"]

def validate_username(username):
    """Check if username is valid and allowed."""
    if not username:
        raise ValueError("Username required.")
    if username not in ALLOWED_USERS:
        raise PermissionError("User not in allowed list.")

def fetch_github_keys(username):
    """Fetch public keys from GitHub for the given username."""
    url = f"https://github.com/{username}.keys"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            raise requests.HTTPError(f"Failed to fetch keys with status code {response.status_code}")
        print(response.text)
    except requests.RequestException as e:
        raise ConnectionError(f"Error fetching keys from GitHub: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <username>", file=sys.stderr)
        sys.exit(1)

    username = sys.argv[1]

    try:
        validate_username(username)
        fetch_github_keys("fuomag9")
    except (ValueError, PermissionError, FileNotFoundError, ConnectionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()