from myproject.chord import Chord

class Triad(Chord):
    def __init__(self, scale2, root_note):
        self.chord_length = 3
        super().__init__(scale2, root_note)


def get_chord_length(self):
        return self.chord_length
