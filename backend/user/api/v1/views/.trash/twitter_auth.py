# Import the necessary modules
from flask import Flask, request, redirect, session, url_for
from api.v1.views import app_views
from models.user import User
from models import storage
import os
from requests_oauthlib import OAuth1Session

# Define your Twitter OAuth credentials
TWITTER_OAUTH_CLIENT = os.getenv('TWITTER_OAUTH_CLIENT')
TWITTER_OAUTH_CLIENT_SECRET = os.getenv('TWITTER_OAUTH_CLIENT_SECRET')

# Define your Twitter callback URL
TWITTER_CALLBACK_URL = 'http://localhost:5000/api/v1/user/twitter/callback'

# Define your Twitter API URLs
TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
TWITTER_AUTHORIZE_URL = 'https://api.twitter.com/oauth/authenticate'

# Define your Flask routes
@app_views.route('/twitter')
def twitter_auth():
    # Create an OAuth1Session instance with the callback URI
    twitter = OAuth1Session(
        TWITTER_OAUTH_CLIENT,
        client_secret=TWITTER_OAUTH_CLIENT_SECRET,
        callback_uri=TWITTER_CALLBACK_URL
    )

    # Fetch the request token
    fetch_response = twitter.fetch_request_token(TWITTER_REQUEST_TOKEN_URL)

    # Extract the request token and secret
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')

    # Save the request token and secret in the session
    session['resource_owner_key'] = resource_owner_key
    session['resource_owner_secret'] = resource_owner_secret

    # Generate the authorization URL
    authorization_url = twitter.authorization_url(TWITTER_AUTHORIZE_URL)

    # Redirect the user to the authorization URL
    return redirect(authorization_url)

@app_views.route('/twitter/callback')
def twitter_callback():
    # Retrieve the request token and secret from the session
    resource_owner_key = session.get('resource_owner_key')
    resource_owner_secret = session.get('resource_owner_secret')

    # Extract the OAuth verifier from the request
    oauth_verifier = request.args.get('oauth_verifier')

    # Create an OAuth1Session instance
    twitter = OAuth1Session(
        TWITTER_OAUTH_CLIENT,
        client_secret=TWITTER_OAUTH_CLIENT_SECRET,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=oauth_verifier
    )

    # Fetch the access token
    access_tokens = twitter.fetch_access_token(TWITTER_ACCESS_TOKEN_URL)

    # Get the user's email from Twitter
    response = twitter.get('https://api.twitter.com/1.1/account/verify_credentials.json',
                         params={'include_email': 'true'})
    response_json = response.json()
    email = response_json['email']

    # Create a new user and save it
    user = User(email=email)
    storage.new(user)
    storage.save()

    # Redirect the user to the index page
    return redirect(url_for('index'))