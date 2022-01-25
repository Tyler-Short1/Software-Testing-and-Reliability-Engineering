class Car:
    def __init__(self, currentspeed, maxspeed, fuellevel):
        self.currentspeed = currentspeed
        self.maxspeed = maxspeed
        self.fuellevel = fuellevel

    def accelerate(self):
        if self.currentspeed < self.maxspeed:
            self.currentspeed+1
            self.fuellevel-1

    def brake(self):
        self.currentspeed-1

    def refuel(self):
        self.fuellevel+1