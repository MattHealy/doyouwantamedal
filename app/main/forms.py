from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, TextAreaField


class AwardForm(FlaskForm):
    name = TextField()
    award = TextAreaField()
    submit = SubmitField('Submit')
