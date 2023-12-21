from flask import Blueprint

bp = Blueprint('errors', __name__)

# Keep import at bottom to avoid circular dependencies
from app.errors import handlers
