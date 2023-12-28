from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    post = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')


class CrewForm(FlaskForm):
    crew_name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Create')


class EnrollForm(FlaskForm):
    crew_name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Enroll')
