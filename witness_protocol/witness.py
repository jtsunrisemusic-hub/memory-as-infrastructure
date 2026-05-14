class Witness:

    def __init__(self, observer, place):
        self.observer = observer
        self.place = place

    def observe(self, observation):

        record = {
            "observer": self.observer,
            "place": self.place,
            "observation": observation,
        }

        return record
