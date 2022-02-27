import os
from pathlib import Path
import pandas as pd
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from sqlalchemy import MetaData


db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
csrf._exempt_views.add('dash.dash.dispatch')

def create_app(config_classname):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_classname)

    db.init_app(flask_app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(flask_app)
    csrf.init_app(flask_app)

    with flask_app.app_context():
        from flask_app.models import User, Post
        db.create_all()
        #db.Model.metadata.reflect(db.engine)
        
        from dash_app.dash_app import init_dashboard
        flask_app = init_dashboard(flask_app)

    return flask_app