x=[[1,2,3],["a","b","c"]]
for i in x:
    for j in i:
        print(j,end="")
    print()

#pattern printing
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#list sum
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))

a=[]
for i in range(r):
    val=[]
    for j in range(c):
        val.append(int(input("Enter a[%d][%d]:"%(i,j))))
    a.append(val)
b=[]
for i in range(r):
    val=[]
    for j in range(c):
        val.append(int(input("Enter b[%d][%d]:"%(i,j))))
    b.append(val)
result=[]
for i in range(r):
    val=[]
    for j in range(c):
        val.append(a[i][j]+b[i][j])
    result.append(val)
print("Sum =",result)








