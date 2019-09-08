

class Keyboard:
    def __init__(self):
        self.key_dict = {}
        self.make_keyboard_distances()


    def make_keyboard_distances(self):
        keys_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        x_position = 0
        for set_number in range(1, 8):
            for key in keys_list:
                self.key_dict[key + str(set_number)] = x_position
                self.key_dict[key + '#' + str(set_number)] = x_position + 5
                if x_position > 0:
                    self.key_dict[key + 'b' + str(set_number)] = x_position - 5
                x_position += 10


    # used for first chord to determine. Other chords will use this distance
    # marker and try to minimize distance to the marker.
    # Ex.
    # Input: ['C', 'E', 'G']
    # Output: 250.0
    def get_x_position_average(self, chord_notes):
        x_pos_sum = 0
        note_counter = 0
        for key in chord_notes:
            octave = key[0]
            note = key[1]
            x_pos_sum += self.key_dict[note + str(octave)]
            note_counter += 1
        x_pos_avg = x_pos_sum / note_counter
        return x_pos_avg


    # comparison used for insertion sort. Puts keys in proper order
    # Ex.
    # input: ['A#5', 'B4']
    # output: True
    def first_note_is_higher_on_keyboard(self, note_1, note_2):
        # print("note1 = {} || note2 = {}".format(note_1, note_2))
        note_1_octave = ''
        note_2_octave = ''
        note_1_octave = note_1[0]
        note_2_octave = note_2[0]
        if int(note_1_octave) == int(note_2_octave):
            if note_1[1][0] > note_2[1][0]:       # comparing the note letters
                return True
            else:
                return False
        if int(note_1_octave) < int(note_2_octave):
            return False
        return True


    # Finds the closest key to the center of the first chord in the progression
    # find_closest_keys(x_pos_avg, ['F', 'A', 'C'])
    def find_closest_keys(self, x_pos_avg, chord_object):
        closest_key = ''
        closest_chord = []
        chord = chord_object.get_chord()
        starting_octave = chord[0][0]
        for key in chord:
            min_distance = 999999
            octave = key[0]
            note = key[1]
            for nearby_octave in range(starting_octave, starting_octave + 3):
                distance_temp = abs(x_pos_avg - self.key_dict[note + str(
                        nearby_octave)])
                if distance_temp < min_distance:
                    closest_key = [nearby_octave, note]
                    min_distance = distance_temp
            closest_chord.append(closest_key)
        return closest_chord


    # Rearranges the chord after the closest keys have been found. This is where
    # chord inversion happens.
    # Ex.
    # input: ['F4', 'A5', 'C4']
    # output: ['C4', 'F4', 'A5']
    # print("rearrange_ = {}".format(rearrange_entire_chord(['A5', 'F4', 'E4'])))
    def rearrange_entire_chord(self, chord):
        note_list = chord.note_list
        for index in range(1, len(note_list)):
            current_value = note_list[index]
            position = index
            while position > 0 and self.first_note_is_higher_on_keyboard(
                    note_list[position- 1],current_value):
                note_list[position] = note_list[position - 1]
                position -= 1
            note_list[position] = current_value
        return note_list
