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
arr1=[0,1,2,3,4,5,7]
arr2=[6,7,8,9,5]
s6=pd.Series(arr2)
print(s6)
s7=pd.Series(arr1)
print(s7)
s8=s6.add(s7)
print(s8)
s9=s6.div(s7)
print(s9)
print('median',s7.median())
print('max',s7.max())
print('min',s7.min())

#Create dataframe
dates=pd.date_range('today',periods=6)
print(dates)
num_arr=np.random.randn(6,4)
print(num_arr)

columns=['A','B','C','D']
df1=pd.DataFrame(num_arr,index=dates,columns=columns)
print(df1)

#Create dataframe with dictionary array
data={
    'animel':['cat','cat','snake','dog','dog','cat','snake','cat','dog','dog'],
    'age':[2.5,3,0.5,np.nan,7,3,5,3,7,8],'visits':[1,3,2,3,2,3,1,1,2,1],
    'priority':['yes','yes','no','yes','no','no','yes','no','no','yes']
    }
labels=['a','b','c','d','e','f','g','h','i','j']
df2=pd.DataFrame(data,index=labels)
print(df2)

print(df2.dtypes)
print(df2.head(2))
print(df2.tail(2))
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)
print(df2.sort_values(by='age'))

#Slicing dataframe
print(df2.sort_values(by='age')[1:3])

#query dataframe by tag
print(df2[['age','visits']])
print(df2.iloc[1:3])
df3=df2.copy()
print(df3)

print(df3.isnull())

df3.loc['f','age']=1.5
print(df3)

print(df3.sum())

string=pd.Series(['A','C','D','Aaa','Bbb',np.nan,'CAS','cow','owl'])
print(string)
print(string.str.lower())
print(string.str.upper())

#38:57s simplilearn python for beginners
#lesson 9



