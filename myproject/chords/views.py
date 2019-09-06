from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Chord
from myproject.chords.forms import AddForm, DelForm

chords_blueprint = Blueprint('chords',
                              __name__,
                              template_folder='templates/chords')

@chords_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        steps = form.steps.data
        # Add new owner to database
        new_chord = Chord(steps)
        db.session.add(new_chord)
        db.session.commit()

        return redirect(url_for('chords.list'))
    return render_template('add.html',form=form)


@chords_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    chords = Chord.query.all()
    return render_template('list.html', chords=chords)

@chords_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        chord = Chord.query.get(id)
        db.session.delete(chord)
        db.session.commit()

        return redirect(url_for('chords.list'))
    return render_template('delete.html',form=form)
