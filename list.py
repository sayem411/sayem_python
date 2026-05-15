num=[1,2,3]
print(num)
letter=['a','b','c']
print(letter)
stg=["get","certified"]
print(stg)
mix=[1,5,"hi",'a']
print(mix)
mat=[[1,2],['a','b']]
print(mat)
print(mix[2])
print(mix[::-1])
print(mix[:2])
#operation on list
conc=letter+stg
print(conc)
var=list("Hey there")
print(var)
one, *other=num
print(one)
print(other)
#method in list
num.append(4)
print(num)

num.extend(stg)
print(num)

num.insert(3,"simplilearn")
print(num)

num.remove("simplilearn")
print(num)

var1=['a','s','d','f','g']
var1.sort()
print(var1)
var1.sort(reverse=True)
print(var1)

print(var1.reverse())
#Build-in-function with list
x=[9,17,14,4,90,55]
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
print(sum(x)/len(x))

#Movies project
movies=[]
mov1=input("Enter 1st movies")
mov2=input("Enter 2nd movies")
mov3=input("Enter 3rd movies")
 
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)











