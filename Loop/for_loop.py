x=[1,6,"simplilearn"]
for i in x:
    print(i)
y="Simplilearn"
for j in y:
    print(j)

#range
for i in range(1,20,2):
    print(i)
for i in range(0,20,2):
    print(i)
#factorial
n = int(input("Enter a number: "))
product = 1
for i in range(1, n+1):
    product*= i
print(product)
#sum using for loop
sum=0
for i in range(0,21):
    if(i%2==0):
        sum+=i
print(sum)

#reverse using for loop
n = int(input("Enter a number: "))
reverse = 0
for i in range(len(str(n))):  
    reverse = reverse * 10 + n % 10
    n = n // 10
print(reverse)



