#Tuples is collection of immutable heterogeneous python objects
#creating tuples
emp=()
print(type(emp))
print(emp)

city=("Dhaka","Rajshahi","Chittagong")
num=1,2,3,4
print(city)
print(type(city))
print(city[1])
print(city[-1])
print(city+num)

list=[1,2,3]
tuple=(1,2,3)
list.append(4)
print(list) #'tuple' object has no attribute 'append'

#Nesting
nest=(city,num)
print(nest)

#Repetation
rep=("Python",)
print(rep*10)

a,*b,c,d=num
print(a,b,c,d)
#Unpacking
a=tuple("HelloWorld")
for sayem in a:
    print(sayem)

#Built in function
num2=(3,4,2,2,2,2,6,5,8)
print(num2)
print(num2.count(2))
print(sum(num2))
print(len(num2))
print(max(num2))
print(min(num2))

#converting tuple to list
lst=[(1,2,3),(4,5,6)]
print(lst)
lst.append(("Tuple","Inside","List"))
print(lst)
lst.remove((1,2,3))
print(lst)

#converting list to tuples
tpl=(['a','b','c'],['e','f','g'])
print(tpl)

tpl[0].append('d')
print(tpl)
tpl[0].remove('d')
print(tpl)






