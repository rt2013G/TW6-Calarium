from flask import Blueprint

bp = Blueprint('auth', __name__)

# Keep import at bottom to avoid circular dependencies
from app.auth import routes
