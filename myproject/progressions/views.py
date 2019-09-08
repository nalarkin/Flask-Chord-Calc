from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Progression
from myproject.progressions.forms import AddForm, DelForm

progressions_blueprint = Blueprint('progressions',
                              __name__,
                              template_folder='templates/progressions')

@progressions_blueprint.route('/add_progression', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        progression = form.progressions.data
        # Add new owner to database
        new_progression = Progression(progression)
        db.session.add(new_progression)
        db.session.commit()

        return redirect(url_for('progressions.list'))
    return render_template('add_progression.html',form=form)


@progressions_blueprint.route('/list_progressions')
def list():
    # Grab a list of puppies from database.
    progressions = Progression.query.all()
    return render_template('list_progressions.html', progressions=progressions)

@progressions_blueprint.route('/delete_progressions', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        progression = Progression.query.get(id)
        db.session.delete(progression)
        db.session.commit()

        return redirect(url_for('progressions.list'))
    return render_template('delete_progressions.html',form=form)
