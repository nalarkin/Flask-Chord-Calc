# from chord_controller import ChordController


class ChordViewer:
    def __init__(self):
        pass

    def notify_clicked_progression(self, progression):
        self.receive_progression(progression)

    def receive_progression(self, progression):
        print("viewer receive_progression = {}".format(progression))


    # def notify_sig_change(self, sig):
