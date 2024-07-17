# NoPlace Username Availability Checker

This Python script checks the availability of usernames on the NoPlace app using multiple threads and rotates proxies fetched from a proxy API.

## Overview

The script utilizes multithreading to efficiently check the availability of usernames on the NoPlace app. Proxies are rotated to prevent rate limiting and IP bans, ensuring reliable performance during the username checking process.

## Features

- **Multithreaded Processing:** Utilizes multiple threads to check usernames concurrently, enhancing speed and efficiency.
- **Proxy Rotation:** Automatically fetches and rotates proxies to avoid detection and maintain anonymity.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vandalise/noplace-username-checker.git
   cd noplace-username-checker
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Update ``usernames.txt`` with usernames to check

## Usage
Run the script:
    ```bash
    python bot.py
    ```

## Why?

I developed this script to explore potential username availability on the NoPlace app, with the idea of generating usernames for resale if the app gains popularity. Unfortunately, the NoPlace app requires a 2FA (Two-Factor Authentication) code for the login processes. This means if we generate an account we will not be able to login... During the sign-up process, an access token (bearer token) is provided, which allows access to account information. However, leveraging this token to log into the account needs more investigation.
