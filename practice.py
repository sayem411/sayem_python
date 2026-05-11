x = [1, 2.3, "Simplilearn"]
print(len(x)) 

n = int(input("Enter a number: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end='')
        j+=1
    i+=1
    print()

n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j)
    print()



