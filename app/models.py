from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#
# The crew class holds information for a crew, or small groups of user.
# A crew has a derived attribute which is the collective 'power' of all its members
#
class Crew(db.Model):
    crew_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    crew_name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    creation_date: so.Mapped[Optional[datetime]] = so.mapped_column(default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return '<Crew {}>'.format(self.crew_name)


#
# UserMixin is an implementation of users of flask-login
#
class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    about_me: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    last_seen: so.Mapped[Optional[datetime]] = so.mapped_column(default=lambda: datetime.now(timezone.utc))
    power: so.Mapped[int] = so.mapped_column(sa.Integer, default=0)
    crew_user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Crew.crew_id), nullable=True)

    messages_sent: so.WriteOnlyMapped['Message'] = so.relationship(foreign_keys='Message.sender_id',
                                                                   back_populates='author')
    messages_received: so.WriteOnlyMapped['Message'] = so.relationship(foreign_keys='Message.recipient_id',
                                                                       back_populates='recipient')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_messages(self):
        query = self.messages_received.select().order_by(Message.timestamp.desc())
        return db.session.scalars(query)

    def create_crew(self, name):
        crew = Crew(leader_id=self.id)
        crew.crewmates.add(self)
        db.session.add(crew)
        return crew


# The loader function helps to connect flask-login with the database
@login.user_loader
def load_user(login_user_id):
    return db.session.get(User, int(login_user_id))


class Message(db.Model):
    message_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    sender_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    recipient_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(512))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))

    author: so.Mapped[User] = so.relationship(foreign_keys='Message.sender_id', back_populates='messages_sent')
    recipient: so.Mapped[User] = so.relationship(foreign_keys='Message.recipient_id',
                                                 back_populates='messages_received')

    def __repr__(self):
        return '<Message {}>'.format(self.body)
