import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

import os
import re




database_url = os.environ.get('DATABASE_URL', None)

if database_url:
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        # rest of connection code using the connection string `uri`

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(basedir, '../app.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'fill-in-with-secret-key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, controllers