from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# This tells flask login which function handles the login, the name is the same one would use in a url_for()
login.login_view = 'login'
moment = Moment(app)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.main import bp as main_bp
app.register_blueprint(main_bp)

# Keep import at bottom to avoid circular dependencies
from app import models
