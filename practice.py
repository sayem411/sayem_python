r=int(input("Enter number of rows:"))
c=int(input("Enter number of column:"))
a=[]
for i in range(r):
    val=[]
    for j in range(c):
        val.append(int(input("Enter a[%d][%d]"%(i,j))))
    a.append(val)
b=[]
for i in range(r):
    val=[]
    for j in range(c):
        val.append(int(input("Enter b[%d][%d]"%(i,j))))
    b.append(val)
result=[]
for i in range(r):
    val=[]
    for j in range(c):
        val.append(a[i][j]+b[i][j])
    result.append(val)
print("Sum=",result)
