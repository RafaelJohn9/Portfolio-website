#!/usr/bin/env python3
"""
Used in Google Oauth
"""
from flask import redirect, url_for, session
from flask_oauthlib.client import OAuth
from models import storage
from models.user import User
from api.v1.views import app_views
import os
from flask import request
from flask_login import login_user
from flask import jsonify

oauth = OAuth(app_views)

google = oauth.remote_app(
    'google',
    consumer_key=os.environ.get('GOOGLE_OAUTH_CLIENT'),
    consumer_secret=os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


@app_views.route('/google')
def google_login():
    """
    google login
    """
    try:
        return google.authorize(callback=url_for('app_views.authorized',
                                _external=True))
    except Exception as e:
        return "An error occurred during Google login"


@app_views.route('/google/authorized')
@google.authorized_handler
def authorized(resp):
    """
    authorization handler
    """
    try:
        if resp is None:
            return 'Access denied: reason=%s error=%s' % (
                request.args['error_reason'],
                request.args['error_description']
            )
        session['google_token'] = (resp['access_token'], '')
        me = google.get('userinfo')
        user_email = me.data['email']

        user = storage.get(User, email=user_email)
        if user is None:
            user = User(email=user_email)
            try:
                storage.new(user)
                storage.save()
            except Exception as e:
                return jsonify(
                                {"error":
                                    "An error occurred during user creation"}
                                ), 500
        login_user(user)
        return redirect('http://localhost:3000/')
    except Exception as e:
        return "An error occurred during authorization"


@google.tokengetter
def get_google_oauth_token():
    """
    Gets the google oauth token
    """
    try:
        return session.get('google_token')
    except Exception as e:
        return None
