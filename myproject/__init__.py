import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# from myproject.chord_controller import ChordController
# chord_controller = ChordController()

from myproject.new_chord import NewChordController
chord_controller = NewChordController()

# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.
## Grab the blueprints from the other views.py files for each "app"
from myproject.chords.views import chords_blueprint
from myproject.progressions.views import progressions_blueprint

# from myproject.owners.views import owners_blueprint
#
app.register_blueprint(chords_blueprint,url_prefix="/chords")
app.register_blueprint(progressions_blueprint,url_prefix="/progressions")

# app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
