

class Scale():
    def __init__(self):
        self.all_keys = ''
        self.scale_size = 7
        self.note_tracker = ''
        self.major_scale_steps = [2, 2, 1, 2, 2, 2, 2]


    def get_all_keys(self):
        # print("scaleprovided: {}".format(self.))
        return self.all_keys


    def get_notes(self):
        return self.current_scale_notes


    def iterate_keys(self, note_tracker, steps):
        self.note_tracker = note_tracker
        self.goes_past_last_key_in_scale(steps)
        return self.note_tracker


    def goes_past_last_key_in_scale(self, steps):
        index =  self.get_all_keys().index(self.note_tracker)
        scale_max = 11
        jump_in_notes = index + steps
        if jump_in_notes > scale_max:
            self.note_tracker = self.all_keys[jump_in_notes - scale_max]
        else:
            self.note_tracker= self.all_keys[jump_in_notes]


    def build_scale(self, scale_root='C'):
        self.current_scale_notes = []
        flats = False
        flat_key_sigs = ['F', 'Bb', 'Eb', 'Ab', 'Db','Gb', 'Cb']
        if flat_key_sigs.__contains__(scale_root):
            self.all_keys = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb','B']
            flats = True
        else:
            self.all_keys =  ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        scale_note_tracker = self.all_keys.index(scale_root)
        for step in self.major_scale_steps:
            if flats:
                self.current_scale_notes.append(self.all_keys[scale_note_tracker])
            else:
                self.current_scale_notes.append(self.all_keys[scale_note_tracker])
            scale_note_tracker += step
            # scale circles back to start of list
            if scale_note_tracker >= len(self.all_keys) - 1:
                scale_note_tracker -= 12
