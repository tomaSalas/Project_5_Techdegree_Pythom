from flask_wtf import Form
from wtforms import (StringField, PasswordField, TextAreaField,
                     DateField, IntegerField)

from wtforms.validators import (DataRequired, Regexp, ValidationError,
                                Email, Length, EqualTo)
from models import Entry


def title_exists(form, field):
    """ cheack if an entry exits already"""
    if Entry.select().where(Entry.title == field.data).exists():
        raise ValidationError('Entry with that title already exists.')


class new_entry(Form):
    title = StringField(
        'Title',
        validators=[
            DataRequired(),
            title_exists
        ]
    )
    date = DateField(
        'Date (yyyy-mm-dd)',
        validators=[
            DataRequired()
        ]
    )
    time_spent = IntegerField(
        'Time Spent (in minutes)',
        validators=[
            DataRequired()
        ]
    )
    learned = TextAreaField(
        'What I Learned',
        validators=[
            DataRequired()
        ]
    )
    resources = TextAreaField(
        'Resources to Remember (resource name, space, url)',
        validators=[
            DataRequired()
        ]
    )
    tags = StringField(
        'Tags (separate with a space)',
    )


class edit_entry(Form):
    title = StringField(
        "Title",
        validators=[
            DataRequired(),
        ]
    )
    date = DateField(
        "Date (yyyy-mm-dd)",
        validators=[
            DataRequired()
        ]
    )
    time_spent = IntegerField(
        "Time Spent (in minutes)",
        validators=[
            DataRequired()
        ]
    )
    learned = TextAreaField(
        "What I Learned",
        validators=[
            DataRequired()
        ]
    )
    resources = TextAreaField(
        "Resources to Remember (resource name, space, url)",
        validators=[
            DataRequired()
        ]
    )
    tags = StringField(
        "'Tags (separate with a spaces)",
    )


class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
