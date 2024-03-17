#!/usr/bin/env python3
import uuid
from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth
from models import storage
from models.user import User
from api.v1.views import app_views
import os
from flask import request

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
def login():
    return google.authorize(callback=url_for('app_views.authorized', _external=True))

@app_views.route('/google/authorized')
@google.authorized_handler
def authorized(resp):
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
        storage.new(user)
    session_token = str(uuid.uuid4())
    return session_token

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')