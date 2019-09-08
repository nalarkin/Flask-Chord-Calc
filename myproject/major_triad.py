from myproject.triad import Triad

class MajorTriad(Triad):
    def __init__(self, scale2, root_note):
        super().__init__(scale2, root_note)
        self.index_to_build = [0, 4, 3]
        self.build_chord()
        self.chord_type = "Major"