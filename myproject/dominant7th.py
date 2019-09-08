from myproject.chord import Chord

class Dominant7th(Chord):
    def __init__(self, scale2, root_note):
        self.chord_length = 4
        super().__init__(scale2, root_note)


def get_chord_length(self):
    return self.chord_length
