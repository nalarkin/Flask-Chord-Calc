# TODO: FIND WAY TO QUERY CHORDS
# TODO: CHECK how to find dominant chords. When should I calculate this?
# TODO: change storage to have chord types "like V, IV" as the chord rows
# TODO: change chord calculation to rotate to correct pos (ex. C major = G)
#  before creating chord

from myproject import db
from myproject import chord_controller

class Chord(db.Model):
        __tablename__ = 'chords'
        id = db.Column(db.Integer,primary_key = True)
        steps = db.Column(db.Text)
        sig_c = db.Column(db.Text)
        sig_g = db.Column(db.Text)
        sig_d = db.Column(db.Text)
        sig_a = db.Column(db.Text)
        sig_e = db.Column(db.Text)
        sig_b = db.Column(db.Text)
        sig_f_sharp = db.Column(db.Text)
        sig_c_sharp = db.Column(db.Text)

        sig_f = db.Column(db.Text)
        sig_b_flat = db.Column(db.Text)
        sig_e_flat = db.Column(db.Text)
        sig_a_flat = db.Column(db.Text)
        sig_d_flat = db.Column(db.Text)
        sig_g_flat = db.Column(db.Text)

        # scale = db.relationship('Scale',backref='chord',uselist=False)

        def __init__(self,steps):
            steps_list = steps.split(",")
            for index in range(len(steps_list)):
                steps_list[index] = steps_list[index].strip()
            self.steps = str(steps_list)

            generated_chords = chord_controller.create_12_chords(steps_list)

            self.sig_c = str(generated_chords[0]).strip('[]')
            self.sig_g = str(generated_chords[1]).strip('[]')
            self.sig_d = str(generated_chords[2]).strip('[]')
            self.sig_a = str(generated_chords[3]).strip('[]')
            self.sig_e = str(generated_chords[4]).strip('[]')
            self.sig_b = str(generated_chords[5]).strip('[]')
            self.sig_f_sharp = str(generated_chords[6]).strip('[]')
            self.sig_c_sharp = str(generated_chords[7]).strip('[]')
            self.sig_f = str(generated_chords[8]).strip('[]')
            self.sig_b_flat = str(generated_chords[9]).strip('[]')
            self.sig_e_flat = str(generated_chords[10]).strip('[]')
            self.sig_a_flat = str(generated_chords[11]).strip('[]')
            self.sig_d_flat = str(generated_chords[12]).strip('[]')
            self.sig_g_flat = str(generated_chords[13]).strip('[]')

        def __repr__(self):
            # if self.scale:
            #     return f"Chord is {self.steps} and scale is {self.scale.name}"
            # else:
                # return f"Chord name is {self.steps} and has no scale
            return f"Chord steps is {self.steps} and sig column examples are " \
                   f"{self.sig_a} and {self.sig_d_flat}"

class Progression(db.Model):
        __tablename__ = 'progressions'
        id = db.Column(db.Integer,primary_key = True)
        progression = db.Column(db.Text)
        # scale = db.relationship('Scale',backref='chord',uselist=False)


        def __init__(self,chords):
            # self.progression = chord_controller.receive_new_progression(chords)
            pass

        def __repr__(self):
            return f"Progression name is {self.progression} and has no scale"
