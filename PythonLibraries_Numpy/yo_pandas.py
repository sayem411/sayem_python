import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6,4), index=list(range(6)), columns=list('ABCD'))
print(df)
print(df.describe())

#check pandas version
print(pd.__version__)

#Series create,manipulate,querry,delete
#creating a series from a list
arr=[0,1,2,3,4]
s1=pd.Series(arr)
print(s1)

order=[1,2,3,4,5]
s2=pd.Series(arr,index=order)
print(s2)

#Create a random Ndarray
import numpy as np
n=np.random.randn(5)
index=['a','b','c','d','e']
s2=pd.Series(n,index=index)
print(s2)

#create series from dictionary
d={'a':1,'b':2,'c':3,'d':4,'e':5}
s3=pd.Series(d)
print(s3)

#you can modify the index of series
print(s1)
s1.index=['A','B','C','D','E']
print(s1)

#slicing
a=s1[:3]
print(a)
a=s1[:-1]
print(a)
a=s1[2:]
print(a)
s4=pd.concat([s1,s3])
print(s4)
s5=s4.drop('e')
print(s5)

#Series operation





