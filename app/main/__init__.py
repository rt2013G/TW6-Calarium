from flask import Blueprint

bp = Blueprint('main', __name__)

# Keep import at bottom to avoid circular dependencies
from app.main import routes
