from myproject.scale import Scale
from myproject.major_triad import MajorTriad
from myproject.minor_triad import MinorTriad
from myproject.diminished_triad import Diminished
from myproject.major_dom_7th import MajorDom7th


class ChordModel:
    def __init__(self):
        self.build_new_scale()


    def get_scale(self):
        return self.current_scale


    # IF ADDING NEW CHORD ADD IT TO THE LISTS AND DICTIONARY BELOW
    def build_progression(self, progression):
        major_chords = ["I", "IV", "V"]
        minor_chords = ["ii", "iii", "vi"]
        dim_chords = ['vii']
        dom_chords = ['V7']
        scale_degree_convert = {'I': 1, 'ii': 2, 'iii': 3, 'IV': 4, 'V': 5,
                                'vi': 6, 'vii': 7, 'V7': 5}
        self.built_progression = []
        for chord in progression:
            chord_note = scale_degree_convert[chord]
            chord_note = self.convert_degree_to_note(chord_note)

            if chord in major_chords:
                new_chord = MajorTriad(self.current_scale, chord_note)
            if chord in minor_chords:
                new_chord = MinorTriad(self.current_scale, chord_note)
            if chord in dim_chords:
                new_chord = Diminished(self.current_scale, chord_note)
            if chord in dom_chords:
                new_chord = MajorDom7th(self.current_scale, chord_note)

            self.built_progression.append(new_chord)
        return self.built_progression


    def convert_degree_to_note(self, degree):
        scale = self.current_scale.get_notes()
        return scale[degree - 1]


    def build_new_scale(self, root_note='C'):
        self.current_scale = Scale()
        self.current_scale.build_scale(root_note)


    def print_notes(self, progression):
        pass


    def calculate_x_average(self, progression):
        pass
