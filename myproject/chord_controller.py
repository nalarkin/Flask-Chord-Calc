from myproject.chord_viewer import ChordViewer
from myproject.chord_model import ChordModel
from myproject.keyboard import Keyboard


# create instances of viewr, model, and controller
# initiate application here


class ChordController:
    def __init__(self):
        self.chord_model = ChordModel()
        self.chord_view = ChordViewer()
        self.keyboard = Keyboard()
        self.chord_model.build_new_scale('E')


    def receive_new_progression(self, progression):
        self.roman_numeral_prog = progression.split()
        print("chordcontroller receive_new_progression: {}".format(progression.split()))
        self.prog_chords = self.chord_model.build_progression(progression.split())
        self.calculate_starting_position()
        self.improve_progression_voice_leading()
        self.reoder_improved_chord()
        self.print_progression()
        return "IT WORKED!"


    def print_notes(self):
        for chord in self.prog_chords:
            print(chord.get_chord())


    def calculate_starting_position(self):
        first_chord = self.prog_chords[0]
        self.x_pos_avg = self.keyboard.get_x_position_average(
                first_chord.get_chord())


    def get_scale(self):
        return self.prog_chords[0].scale


    # def create_progression(self, progression):
    #     pass


    def print_progression(self):
        print("==========================")
        print("print_progression called")
        progression_progress_counter = 0
        for chord in self.prog_chords:
            print("{} - {} {}: {}".format(self.roman_numeral_prog[
                                              progression_progress_counter],
                                              chord.get_root_note(),
                                              chord.get_chord_type(),
                                              chord.get_chord()))
            progression_progress_counter += 1
        print("==========================")

        return self.prog_chords



    def built_progression_root(self, progression):
        self.built_progression_root = progression


    def improve_progression_voice_leading(self):
        improved_progression = []
        for chord in self.prog_chords:
            improved_chord = self.keyboard.find_closest_keys(self.x_pos_avg,
                                                           chord)
            chord.set_notes(improved_chord)
            improved_progression.append(chord)
        self.prog_chords = improved_progression


    def reoder_improved_chord(self):
        reordered_progression = []
        for chord in self.prog_chords:
            reordered_chord = self.keyboard.rearrange_entire_chord(chord)
            reordered_progression.append(reordered_chord)


    def receive_inverted_progression(self, progression):
        self.built_progression = progression


    def create_printed_notes(self):
        ChordModel.print_notes(self.built_progression)


    def receive_printed_notes(self, printed_notes):
        self.update_viewer(printed_notes)


    def update_viewer(self):
        ChordViewer.receive_progression(self.built_progression)


    def update_scale(self, scale_root):
        self.chord_model.build_new_scale(scale_root)
