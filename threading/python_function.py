def func1(*args,**kwargs):
    for i in kwargs.items():
        print(i)
func1(a=10,b=20,c=30)
#------------------------------
def func1():
    x=10
    def func2(x):
        return x+1
    return func2(x)
result=func1()
print(result)
#------------------------------
def func1(called_func):
    print("This is the function")
    def nested_func1(called_func):
        print("This is the nested function")
        called_func()
    return nested_func1(called_func)
def outer_func():
    print("This is the outer function")
obj=func1(outer_func)

#factory-class
B=type("Baseclass",(object,),{})
c1=type("C1",(B,),{'val':5})
c2=type("C2",(B,),{'val':10})

def ClassCreator(bool):
    if bool:
        return c1()
    else:
        return c2()
print(ClassCreator(True).val)
print(ClassCreator(False).val)
