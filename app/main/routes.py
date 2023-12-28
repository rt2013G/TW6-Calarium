from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
import sqlalchemy as sa
from app import db
from app.main import bp
from app.models import User, Post
from app.main.forms import PostForm


@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect((url_for('main.home')))
    return render_template('index.html')


@bp.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    return render_template('user.html', user=user)


@bp.route('/soon')
@login_required
def soon():
    return render_template('errors/coming-soon.html')


@bp.route('/play')
@login_required
def play():
    return render_template('play.html')


@bp.route('/crew')
@login_required
def crew():
    return render_template('crew.html')


@bp.route('/inbox')
@login_required
def inbox():
    query = sa.select(Post).order_by(Post.timestamp.desc())
    posts = db.session.scalars(query)
    return render_template('inbox.html', posts=posts)


@bp.route('/send_message', methods=['GET', 'POST'])
@login_required
def send_message():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.inbox'))
    return render_template('send-message.html', form=form)


@bp.route('/leaderboard')
@login_required
def leaderboard():
    return render_template('leaderboard.html')
