# Flask Google OAuth Example

This project demonstrates how to implement Google OAuth authentication in a Flask application. <br>
Users can log in using their Google account, and access protected routes only available to authenticated users.<br>

## Features

- Google OAuth 2.0 integration
- User session management
- Protected routes accessible only by authenticated users
- Simple frontend with login/logout functionality

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed
- A Google Cloud Platform account
- OAuth 2.0 credentials configured in Google Cloud Console

## Installation

To set up the project environment, follow these steps:

1. **Clone the repository:**

```sh
git clone https://github.com/yourusername/flask-google-oauth-example.git
cd flask-google-oauth-example
```

2. **Setup and acitvate virtual environment and install dependencies:**

```sh
pip install pipenv
pipenv --python 3.8
pipenv shell
pipenv install Flask Authlib
```