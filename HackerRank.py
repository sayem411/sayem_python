#1. Say hello world
s="Hello, World!"
print(s)
#2. if-else
n = int(input().strip())

if n%2!=0:
    print("Weird")
elif n in range(2,6):
    print("Not Weird")
elif n in range(6,21):
    print("Weird")
elif n>20:
    print("Not Weird")
#3. arithmatic operators
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
#4. division
a=int(input())
b=int(input())
print(a//b)
print(a/b)
#5. loops
n = int(input())
for i in range(n):
    print(i * i)

