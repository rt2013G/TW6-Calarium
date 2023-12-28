import random
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
import sqlalchemy as sa
from app import db
from app.main import bp
from app.models import User, Post, Crew
from app.main.forms import PostForm, CrewForm, EnrollForm


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


@bp.route('/add_coins/<username>')
def add_coins(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    coins = random.randint(0, 500)
    user.power += coins
    db.session.commit()
    return render_template('play.html', coins=coins)


@bp.route('/crew')
@login_required
def crew():
    crew_id = current_user.crew_user_id
    if crew_id is None:
        return redirect(url_for('main.create_crew'))
    crew = db.first_or_404(sa.select(Crew).where(Crew.crew_id == crew_id))
    crewmates = db.session.scalars(sa.select(User).where(User.crew_user_id == crew_id).order_by(User.power))
    wealth = 0
    for crewmate in crewmates:
        wealth += crewmate.power

    return render_template('crew.html', crew=crew, wealth=wealth)


@bp.route('/create_crew', methods=['GET', 'POST'])
@login_required
def create_crew():
    crew_form = CrewForm()
    if crew_form.validate_on_submit():
        name = crew_form.crew_name.data
        crew = Crew(crew_name=name)
        db.session.add(crew)
        db.session.commit()
        return redirect(url_for('main.enroll', crew_name=name))

    return render_template('crewless.html', crew_form=crew_form)


@bp.route('/enroll/', methods=['GET', 'POST'])
@login_required
def enroll():
    enroll_form = EnrollForm()
    if enroll_form.validate_on_submit():
        crew_id = db.session.scalar(sa.select(Crew).where(Crew.crew_name == enroll_form.crew_name.data)).crew_id
        current_user.crew_user_id = crew_id
        db.session.commit()
        return redirect(url_for('main.crew'))
    return render_template('enroll.html', enroll_form=enroll_form)


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
    query = sa.select(User).order_by(User.power.desc())
    users = db.session.scalars(query)
    return render_template('leaderboard.html', users=users)
