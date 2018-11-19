from InputReader import InputReader
from Responder import Responder

class SupportSystem:
    def __init__ (self):
        self.reader = InputReader()
        self.responder = Responder()

    def start(self):
        finished = False

        self.printWelcome()

        while not finished:
            user_input = self.reader.getInput()
            if user_input.startswith('bye'):
                finished = True
            else:
                self.response = self.responder.generateResponder()
                print(self.response)

        self.printGoodbye()

    def printWelcome(self):
        print("Welkom bij de immalle helpdienst!")
        print("Vertel je probleem...")
        print("om te stoppen type 'bye'")
    
    def printGoodbye(self):
        print("tot ziens!")

