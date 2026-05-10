import numpy as np
a=np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)

b=np.arange(12).reshape(3,4)
print(b)
b.reshape(3,4)
print(b)
#numpy vs python list
import time
import sys
c=range(1000)
print(sys.getsizeof(5)*len(c))

d=np.arange(1000)
print(d.size*d.itemsize)

size=1000000
L1=range(size)
L2=range(size)
A1=np.arange(size)
A2=np.arange(size)
start=time.time()
result=[(x+y) for x,y in zip(L1,L2)]
result=[(x+y) for x,y in zip(L1,L2)]
print(result)
print("Python list tool:",(time.time() -start)*1000)

start = time.time()
result=A1 +A2
print(result)




