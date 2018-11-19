from random import choice

class Responder:
    def __init__(self):
        self.responses = []
        self.fillResponses()

    def generateResponder(self):
        return choice(self.responses)

    def fillResponses(self):
        self.responses.append("Wow!")
        self.responses.append("Echt?")
        self.responses.append("leuk!")
        self.responses.append("cool")