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

#Build-in-function with list
x=[9,17,14,4,90,55]
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
print(sum(x)/len(x))












