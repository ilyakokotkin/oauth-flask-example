#./oauth-flask-example/app.py

"""
You need to have a Google Cloud Platform account and create a project 
in the Google API Console. Within this project, you'll create OAuth 2.0 credentials 
(Client ID and Client Secret) and set the authorized redirect URIs to your 
application's redirect endpoint.
"""

from flask import Flask, redirect, url_for, session, request
from functools import wraps
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
# Secret key required for session
app.secret_key = 'your_secret_key'

# Configure OAuth
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    # Amend scopes according to OAuth credentials scope. Sometimes this can cause an error
    # if scopes are hardcoded in Flask but are not selected on the Google side
    client_kwargs={'scope': 'openid profile email'},
)

# Authorization check function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    email = dict(session).get('email', None)
    return f"Hello, {'not logged in' if email is None else email}"

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/auth/redirect')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['email'] = user_info['email']
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
