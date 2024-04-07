from flask import Blueprint

"""
contains app_views that has the blueprint for the app
"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1/user')

# from api.v1.views.create_user  import *
# from api.v1.views.google_auth  import *
# from api.v1.views.login import *
# from api.v1.views.user_loggedin import *
from api.v1.views.homepage import *
from api.v1.views.recommendations_search import * 
from api.v1.views.recommendations_recommend import *
from api.v1.views.recommendations_recommended import *
