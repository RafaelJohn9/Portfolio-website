from api.v1.views import app_views 
from models.user import User
from models import storage
from flask import request, jsonify
from os import environ
from linkedin import linkedin


@app_views.route('/linkedin', methods=['POST'])
def linkedin_auth():
    auth = linkedin.LinkedInAuthentication(
        environ['LINKEDIN_CLIENT_ID'], 
        environ['LINKEDIN_CLIENT_SECRET'], 
        'http://localhost:5000/linkedin', 
        linkedin.PERMISSIONS.enums.values()
    )
    app = linkedin.LinkedInApplication(auth)
    linkedin_email = app.get_profile(selectors=['email-address'])

    new_user = User(email=linkedin_email)
    storage.new(new_user)
    storage.save()

    return jsonify(new_user.to_dict()), 201