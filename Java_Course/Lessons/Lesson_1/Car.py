class Car():
    def __init__(self ,year, foul):
        self.year = year
        self.foul = foul
    
    def run(self):
        while self.foul < 0:
            print("foul level: ", self.foul)
            self.foul -= 1



