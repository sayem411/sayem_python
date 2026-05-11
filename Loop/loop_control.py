x="Hey there. How are you?"
for i in x:
    if i==".":
        break
    print(i,end="")
print("")

a=[1,2,45,12,5,6]
for j in a:
    if j>10:
        continue
    else:
        print(j)