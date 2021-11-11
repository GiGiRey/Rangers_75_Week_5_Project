from flask import Flask
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from .models import db as root_db

app = Flask(__name__)



app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app,root_db)

app.config.from_object(Config)

CORS(app)