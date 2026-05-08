from threading import *
def show():
    print("This is a child thread")
t=Thread(target=show())
t.start()
print("This is a parent thread")

#Threading package
from threading import *

