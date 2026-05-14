class WitnessProtocol:

    def __init__(self):
        self.archive = []

    def observe(self, place, observation):
        event = {
            "place": place,
            "observation": observation
        }

        self.archive.append(event)

        print("WITNESS RECORDED")
        print(f"PLACE: {place}")
        print(f"OBSERVATION: {observation}")

    def review_archive(self):
        print("ARCHIVE:")
        for event in self.archive:
            print(event)


witness = WitnessProtocol()

witness.observe(
    "Pike Place Market",
    "Tourist spectacle overlays labor infrastructure."
)

witness.review_archive()
