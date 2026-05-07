class car():
    def __init__(self,year,speed):
        self.year=year
        self.speed=speed
    def getspeed(self):
        print("Maximum speed is:",self.speed)
    def setspeed(self,speed):
        self.speed=speed

BMW=car(2018,155)
FORD=car(2016,140)

class sedan(car):
    def accelerate(self):
        print('137')
    def opentrunk(self):
        print('trunk has opened')

class suv(car): #child class
    def accelerate(self):
        print('127')
Honda=sedan(2018,150)
BMW.getspeed()
Honda.getspeed()
Honda.opentrunk()
Honda.accelerate()
