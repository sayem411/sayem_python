class car():
    def __init__(self,name):
        self.name=name
class sedan(car):     
    def accelerate(self):
        print("150")
class suv(car):       
    def saccelerate(self):
        print("150")

objL=[sedan("Carmy"),suv("Scorpio")]

for obj in objL:
    print("obj.name+ : ",end="")
    obj.accelerate()


