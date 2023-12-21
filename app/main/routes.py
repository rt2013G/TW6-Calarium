from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
import sqlalchemy as sa
from app import db
from app.main import bp
from app.models import User


@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect((url_for('main.home')))
    return render_template('index.html')


@bp.route('/home')
@login_required
def home():
    return render_template('home.html')


@bp.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    return render_template('user.html', user=user)


@bp.route('/soon')
@login_required
def soon():
    return render_template('errors/coming-soon.html')
