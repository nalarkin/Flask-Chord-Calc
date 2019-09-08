from myproject.scale import Scale
from collections import deque


class Chord(Scale):
    def __init__(self, scale2, root_note):
        self.note_list = []
        super().__init__()
        self.scale = scale2
        self.current_scale_notes = scale2.get_notes()
        self.all_keys = scale2.get_all_keys()
        self.note_length = 2
        self.rotate_to_chord_root(root_note)
        self.root_note = root_note

    def __repr__(self):
        note_list = self.note_list
        note_string = ''
        for note in note_list:
            note_string += str(note) + ' '
        return note_string.strip()


    def build_chord(self, octave=4):
        chord = []
        index_sum = 0
        increase_octave_level = False
        for index in self.index_to_build:
            index_sum += index
            chord.append([octave, self.all_keys[index_sum]])
            if self.all_keys.index('C') < index_sum:
                if not increase_octave_level:
                    octave += 1
                    increase_octave_level = True
        self.note_list = chord


    def set_notes(self, new_notes):
        self.note_list = new_notes


    def get_chord(self):
        return self.note_list


    def print(self):
        return self.scale.get_notes()


    def rotate_to_chord_root(self, root):
        d = deque(self.all_keys)
        d.rotate(- self.all_keys.index(root))
        new_all_keys = list(d)
        self.all_keys = new_all_keys


    def get_chord_type(self):
        return self.chord_type

    def get_root_note(self):
        return self.root_note
