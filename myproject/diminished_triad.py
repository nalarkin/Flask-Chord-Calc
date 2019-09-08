from myproject.triad import Triad

class Diminished(Triad):
    def __init__(self, scale2, root_note):
        super().__init__(scale2, root_note)
        self.index_to_build = [0, 3, 3]
        self.build_chord()
        self.chord_type = "Diminished"
