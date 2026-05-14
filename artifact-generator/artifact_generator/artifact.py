class Artifact:

    def __init__(self, title, form, body):
        self.title = title
        self.form = form
        self.body = body

    def display(self):
        print("TITLE:", self.title)
        print("FORM:", self.form)
        print("BODY:")
        print(self.body)


artifact = Artifact(
    "The Broadcast Is Broken",
    "manifesto",
    "Memory persists where systems fail."
)

artifact.display()
