from threading import *
def show():
    print("This is a child thread")
t=Thread(target=show())
t.start()
print("This is a parent thread")

#Threading package
from threading import *
class mythread(Thread):
    def run(self):
        for i in range(5):
            print("\nThis is a child class")
t=mythread()
t.start()
for i in range(5):
    print("\nThis is the main thread")

#obj
from threading import *
class demo:
    def show(self):
        for i in range(5):
            print("\nThis is a child class")
obj=demo()
t=Thread(target=obj.show())
t.start()
for i in range(5):
    print("\nThis is the parent thread")