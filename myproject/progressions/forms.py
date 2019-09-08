from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    progressions = StringField('Enter Chords in the Progression seperated by a space:')
    submit = SubmitField('Add Progression')

class DelForm(FlaskForm):

    id = IntegerField('ID of chord to remove:')
    submit = SubmitField('Remove Progression')
