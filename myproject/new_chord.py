from collections import deque


#TODO: Add a way decide on correct all_keys[] according to b or #key signature
#TODO: Create a way to iterate through every key signature. Append to List of
# notes within list as output that we will send to flask. Ex. [[C, E, G], [F, A, C],....]



class NewChordController():
    def __init__(self):
        self.all_keys_sharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.all_keys_flats = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G',
                               'Ab', 'A', 'Bb', 'B']
        self.major_scale_steps = [2, 2, 1, 2, 2, 2, 2]
        self.sharp_key_signatures = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
        self.flat_key_signatures = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb']


    def find_progression(self, root_note, progression):
        # create list of progression to iterate through
        progression = progression.replace(' ', '')
        progression = progression.split(',')
        built_progression = []
        for chord_name in progression:
            pass
            # convert chord_name into step_list
            # using root note and semitone function, convert chord_name to
            ##### new root note (ex. root = C, chord_name = V, new root = G)
            # query chord  database for one with proper steps, search correct
            ###### column for key signature of new_root

        # for chord in progression_list[]
            # rearrange chords to follow voicing rules
        # return rearranged list of progression_list[]
        pass


    def find_new_root_note(self, root_note, chord_name):
        if root_note in self.sharp_key_signatures:
            starting_keys = self.rotate_keys_to_new_scale(root_note, self.all_keys_sharps)
        else:
            starting_keys = self.rotate_keys_to_new_scale(root_note,
                                                          self.all_keys_flats)

        diatonic_chord_number = self.find_roman_value(chord_name)
        # convert to semitone
        semitone_count = self.convert_scale_steps_to_semitones(str(diatonic_chord_number))

        # find root_note in starting_keys
        # return new root



    def find_chord_type(self, chord_name):
        if chord_name.find('*') != -1:
            return "Diminished"
        if chord_name.isupper():
            return 'Major'
        else:
            return 'Minor'


    def create_12_chords(self, steps):
        steps = self.convert_steps_to_indexes(steps)
        generated_chords_list = []
        for sharp_key_sig in self.sharp_key_signatures:
            new_chord = self.create_new_chord(steps, sharp_key_sig, sharps=True)
            generated_chords_list.append(new_chord)
        for flat_key_sig in self.flat_key_signatures:
            new_chord = self.create_new_chord(steps, flat_key_sig)
            generated_chords_list.append(new_chord)
        # print("completed generated_chords_list = {}".format(generated_chords_list))
        return generated_chords_list




    def create_new_chord(self, steps, root_note, sharps=False):
        # rotated_all_keys = self.rotate_keys_to_new_scale(root_note,
        #                                                 self.all_keys)
        new_chord = []
        if sharps:
            self.all_keys_sharps = self.rotate_keys_to_new_scale(root_note,
                                                 self.all_keys_sharps)
        else:
            self.all_keys_flats = self.rotate_keys_to_new_scale(root_note,
                                                  self.all_keys_flats)

        converted_semitones = self.convert_scale_steps_to_semitones(steps)

        for semitone in converted_semitones:
            if sharps:
                chord_note = self.all_keys_sharps[semitone]
            else:
                chord_note = self.all_keys_flats[semitone]
            # chord_note = rotated_all_keys[step]
            new_chord.append(chord_note)

        print("new_chord = {}".format(new_chord))
        return new_chord

    def rotate_keys_to_new_scale(self, root_note, keys_to_rotate):
        rotating_deque = deque(keys_to_rotate)
        root_note_index = keys_to_rotate.index(root_note)
        rotating_deque.rotate(-root_note_index)
        keys_to_rotate = list(rotating_deque)
        return list(rotating_deque)


    def get_chord_notes(self, steps, rotated_all_keys):
        chord_notes = []
        new_note = ''
        # length_of_step_notes = range(len(steps))
        for step in range(len(steps)):
            new_note = rotated_all_keys[step]
            chord_notes.append(new_note)
        return chord_notes


    def convert_scale_steps_to_semitones(self, steps):
        semitone_list = []
        #for step in the chord
        for step in steps:
            flat_sharp_flag = 0
            step_in_string = str(step).lower()
            if step_in_string.count('b') > 0:
                flat_count = step_in_string.count('b')
                flat_sharp_flag =+ (flat_count * -1)
                step_in_string = step_in_string.replace('b', '')
            if step_in_string.count('#') > 0:
                sharp_count = step_in_string.count('#')
                flat_sharp_flag =+ (sharp_count * 1)
                step_in_string = step_in_string.replace('#', '')
            #sum the first X number of indexes in major_scale_steps, where X
                # = step. EX. step = 2, sum first two index, so index [0]and[1]
                # to total 4
            #append sum to semitone_list[]
            step_in_int = int(step_in_string)
            semitone_list.append(sum(self.major_scale_steps[0:step_in_int % 7]) +
                                 flat_sharp_flag)
        return semitone_list



    def convert_steps_to_indexes(self, steps):
        for i in range(len(steps)):
            step = str(steps[i])
            if step.isdigit():
                steps[i] = int(steps[i])
                steps[i] = steps[i] - 1
            else:
                flats = step.lower().count('b')
                sharps = step.count('#')
                temp_step = step.replace('b', '')
                temp_step = temp_step.replace('#', '')
                temp_step = int(temp_step) - 1
                step = ''
                if flats > 0:
                    for flat in range(flats):
                        step += 'b'
                if sharps > 0:
                    for sharp in range(sharps):
                        step += '#'
                step += str(temp_step)
                steps[i] = step
        return steps


    def __repr__(self):
        return str("This is the controller, not an individual chord")

    def roman_to_decimal(self, str):
        sum = 0
        index = 0
        while (index < len(str)):
            first_value = self.find_roman_value(str[index])
            if (index+1 < len(str)):
                second_value = self.find_roman_value(str[index+1])
                if (first_value >= second_value):
                    sum = sum + first_value
                    index = index + 1
                else:
                    sum = sum + second_value - first_value
                    index = index + 2
            else:
                sum = sum + first_value
                index = index + 1

        return sum

    def find_roman_value(self, roman_numeral):
        if roman_numeral.isdigit():
            return 0
        else:
            roman_numeral = roman_numeral.upper()
            if (roman_numeral == 'I'):
                return 1
            if (roman_numeral == 'V'):
                return 5