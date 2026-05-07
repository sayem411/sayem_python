def welcome():
    print("Good Morning")

def add(a,b):
    print()
    a=2
    b=3
    total=a+b
    print("The sum is:",total)

x=10
y=20
add(x,y)
print("the sum is",x+y)

#Similarly
def add(a=0,b=0):
    total=a+b
    print("The sum is:",total)

add(10)

#sum of all the element at a list using function

def add(*a):
    total=0
    for i in a:
        total=total+i
    print("The sum is:",total)

add(10,20,30,40,50)




