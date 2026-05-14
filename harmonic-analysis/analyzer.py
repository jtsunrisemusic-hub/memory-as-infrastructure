class HarmonicAnalyzer:

    def __init__(self, rhythm, contradiction, memory):
        self.rhythm = rhythm
        self.contradiction = contradiction
        self.memory = memory

    def evaluate(self):

        score = (
            self.rhythm
            + self.memory
            - self.contradiction
        )

        print("HARMONIC SCORE:", score)

        if score > 5:
            print("System stability detected.")

        else:
            print("System distortion increasing.")


analysis = HarmonicAnalyzer(
    rhythm=7,
    contradiction=2,
    memory=5
)

analysis.evaluate()
