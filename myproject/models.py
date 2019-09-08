from myproject import db
from myproject import chord_controller

class Chord(db.Model):
        __tablename__ = 'chords'
        id = db.Column(db.Integer,primary_key = True)
        steps = db.Column(db.Text)
        # scale = db.relationship('Scale',backref='chord',uselist=False)

        def __init__(self,steps):
            self.steps = steps

        def __repr__(self):
            # if self.scale:
            #     return f"Chord is {self.steps} and scale is {self.scale.name}"
            # else:
                # return f"Chord name is {self.steps} and has no scale
            return f"Chord name is {self.steps} and has no scale"

class Progression(db.Model):
        __tablename__ = 'progressions'
        id = db.Column(db.Integer,primary_key = True)
        progression = db.Column(db.Text)
        # scale = db.relationship('Scale',backref='chord',uselist=False)


        def __init__(self,chords):
            self.progression = chord_controller.receive_new_progression(chords)

        def __repr__(self):
            return f"Progression name is {self.progression} and has no scale"
