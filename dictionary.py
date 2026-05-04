d1={}
print(d1)
print(type(d1))

d2={1:"Welcome",2:"to",3:"python"}
print(d2)

d3={"name":"Sayem","age":21,"professional":"student"}
print(d3)

d4=dict({1:"Welcome",2:"to",3:"python"})
print(d4)

d5=dict([(1,"Welcome"),(2,"to"),(3,"python")])
print(d5)

d6={"name":{"first":"AS","last":"Sayem"},"age":21,"professional":"student"}
print(d6)

#Adding element
d={}
d[0]="Welcome"
print(d)

d[1]=("How","are","you")
print(d)

d["name"]="AS"
print(d)

d["Name"]={"first":"AS","last":"Sayem"}
print(d)

#accessing elements
print(d["name"])#print(d["name"]["first"])
print(d.get(1))

#Deleting Elements
print(d.pop(0))
print(d.popitem())

#using built in function
print(d.values())
keys={'a','b','c'}
value=1
print(dict.fromkeys(keys,value))

d.clear()
print(d)






