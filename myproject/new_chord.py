from collections import deque


#TODO: Add a way decide on correct all_keys[] according to b or #key signature
#TODO: Create a way to iterate through every key signature. Append to List of
# notes within list as output that we will send to flask. Ex. [[C, E, G], [F, A, C],....]
#TODO: Test rotate keys to new scale is working, if not, fix it



class NewChordController():
    def __init__(self, steps, root_notes='C'):
        self.all_keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.steps = self.convert_steps_to_indexes(steps)
        self.root_note = root_notes
        self.major_scale_steps = [2, 2, 1, 2, 2, 2, 2]



    def rotate_keys_to_new_scale(self, root_note, key_list):
        rotating_deque = deque(key_list)
        rotating_deque.rotate(root_note)
        return list(rotating_deque)


    def create_new_chord(self, steps, root_note='C'):
        # rotated_all_keys = self.rotate_keys_to_new_scale(root_note,
        #                                                 self.all_keys)
        new_chord = []

        converted_semitones = self.convert_scale_steps_to_semitones(steps)

        for semitone in converted_semitones:
            chord_note = self.all_keys[semitone]
            # chord_note = rotated_all_keys[step]
            new_chord.append(chord_note)

        print(new_chord)
        return str(new_chord)


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
