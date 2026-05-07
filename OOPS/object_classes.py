#class 
class person:
    
    def __init__(self):   
        self.name = "Sayem"
        self.gender = "Male"
        self.age = 17

    def talk(self):
        print("Hi I'm", self.name)
    
    def vote(self):
        if self.age < 18:
            print("I am not eligible for vote")
        else:
            print("I am eligible for vote")
        
obj = person()
obj.talk()
obj.vote()

#class modify
class person:
    
    def __init__(self,n,g,a):   
        self.name =n
        self.gender = g
        self.age = a

    def talk(self):
        print("Hi I'm", self.name)
    
    def vote(self):
        if self.age < 18:
            print("I am not eligible for vote")
        else:
            print("I am eligible for vote")
        
obj1= person("Sayem","Male",19)
obj2= person("Anika","Female",17)
obj1.talk()
obj1.vote()

obj2.talk()
obj2.vote()