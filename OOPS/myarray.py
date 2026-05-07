from array import * 
arr = array('i', [-1,2,3,4,5]) 
print(arr)  
print(arr.buffer_info())
print(arr[2])

for i in arr:
    print(i)

#pointer
for pnt in range(1,4):
    print(pnt,arr[pnt])

#array reverse
arr.reverse()
print(arr)

arr.append(10)
print(arr)

arr = array('i', [-1,2,3,2,4,5]) 
arr.remove(2)
print(arr)

arr = array('i', [-1,2,3,2,4,5])
print(arr[2])
print(arr.index(3))

#array input python
from array import *
arr=array("i",[])
x=int(input("Enter size of array:"))
print("Enter %d elements"%x)
for i in range(x):
    n=int(input())
    arr.append(n)
print(arr)



