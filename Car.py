class Car:
    def __init__(self, currentspeed, maxspeed, fuellevel):
        self.currentspeed = currentspeed
        self.maxspeed = maxspeed
        self.fuellevel = fuellevel

    def accelerate(self, acceleration):
        if self.fuellevel == 0:
            self.currentspeed = 0
            self.acceleration = 0

        elif self.currentspeed + acceleration <= self.maxspeed:
            self.currentspeed += acceleration
            self.fuellevel -=1
        else:
            self.currentspeed = self.maxspeed

    def brake(self, brakespeed):

        if self.currentspeed > 0:
            self.currentspeed -= brakespeed
            if self.currentspeed < 0:
                self.currentspeed = 0

    def refuel(self, refuel):
        if self.fuellevel < 100:
            self.fuellevel += refuel
            if self.fuellevel > 100:
                self.fuellevel = 100
