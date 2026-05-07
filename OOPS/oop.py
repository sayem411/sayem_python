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

BMW.getspeed()
BMW.setspeed(143)
BMW.getspeed()
FORD.getspeed()


