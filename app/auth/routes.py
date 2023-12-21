from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from urllib.parse import urlsplit
from app import db
from app.auth import bp
from app.models import User
from app.auth.forms import LoginForm, RegistrationForm


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect((url_for('main.home')))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == login_form.username.data))
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=login_form.remember_me.data)

        # request.args contains the url to the next page when a user logs in after attempting to view a @login_required
        # page, if there's no next argument, the user gets redirected to the home page, if there is a next argument the
        # if checks whether next is a relative or full URL. A full URL is ignored for security.
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('main.home')
        return redirect(next_page)
    return render_template('login.html', form=login_form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        user = User(username=registration_form.username.data, email=registration_form.email.data)
        user.set_password(registration_form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('register.html', form=registration_form)
