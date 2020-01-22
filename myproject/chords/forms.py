from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    chord_name = StringField('Enter Chord name (Ex. IV, vii*)')
    steps = StringField('Enter Chord Steps seperated by space:')

    submit = SubmitField('Add Chord')

class DelForm(FlaskForm):

    id = IntegerField('ID of chord to remove:')
    submit = SubmitField('Remove Chord')
