def welcome():
    print("Good Morning")

def add(a,b):
    print(id(a),id(b))
    a=2
    b=3
    print(id(a),id(b))
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

#list
def add(lst):
    lst[2]=0
lst=[0,1,2]
print(lst)
add(lst)
print(lst)

#return function
def add(a,b):
    total=a+b
    return total
result=add(10,20)
print("The sum is:",result)


