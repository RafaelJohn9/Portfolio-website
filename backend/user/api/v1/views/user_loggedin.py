from api.v1.views import app_views
from flask import jsonify, redirect, request, url_for
from flask_login import login_required, current_user
from models import storage


@app_views.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    user = current_user
    if user.is_authenticated:
        return jsonify(user.to_dict()), 200
    else:
        return redirect(url_for('login'))