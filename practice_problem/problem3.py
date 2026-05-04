"""
Write a program to check if a number 
entered by the user is odd or even
"""
num=int(input("Enter number:"))
if(num%2==0):
    print("Even")
else:
    print("Odd")
    """
    Write a program to find the greatest of 3 numbers
    entered by the user
    """
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=int(input("Enter c:"))
    if(a>b and a>c):
        print("a is greater.The number is:",a)
    if(b>a and b>c):
        print("b is greater.The number is:",b)
    else:
        print("c is greater. The number is:",c)
"""
Write a program to check 
if a number is multiple of 7 or not
"""
x=int(input("Enter number:"))
if(x%7==0):
    print("Multiple of 7")
else:
    print("Not a Multiple")