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
r=int(input("Enter number of rows:"))
c=int(input("Enter number of Columns:"))
a=[]
val=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j,int(input("Enter the %d * %d element" %(i,j))))
    a.insert(i,val)
    val=[]
b=[]

for i in range(0,r):
    for j in range(0,c):
        val.insert(j,int(input("Enter the %d * %d element" %(i,j))))
    b.insert(i,val)
    val=[]
sum=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j,a[i][j]+b[i][j])
    sum.insert(i,val)
    val=[]
print(sum)








