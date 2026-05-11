val=int(input("Enter a multiple of 7: "))
while(val%7!=0):
    val=int(input("Enter a multiple of 7: "))
else:
    print("%d is a multiple of 7"%val)
#print 10 times
i=1
while i<=10:
    print("Simplilearn")
    i+=1

i=10
while i>=1:
    print("Simplilearn")
    i-=1
#sum of digit even number
i=1
sum=0
while i<=10:
    if i%2==0:
        sum+=i
    i+=1
print(sum)

#reverse using while loop
n = int(input("Enter a number: "))
reverse = 0
while n%10!= 0:         
    reverse = reverse * 10 + n % 10
    n = n // 10 
print(reverse)

#length of a list using while loop
x=[1,2.3,"Simplilearn"]
length=0
i=0
try:
    while x[i]:
        length+=1
        i+=1
except IndexError:
    print(length)

#length of a list 
x = [1, 2.3, "Simplilearn"]
print(len(x)) 

#pattern printed
n = int(input("Enter a number: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end='')
        j+=1
    i+=1
    print()

#Guess the digit using while loop
import random
nump=random.randint(1000,9999)
print(nump)
n = int(input("Enter a 4 digit number: "))
while n!=10:
    num=nump
    correct=0
    while num%10:
        numc=num%10
        nc=n%10
        num=num//10
        n//10
        if numc==nc:
            correct+=1
    if correct==4:
        print("Congrats!You guess it right")
        break
    else:
        print("%d digit were guessed right"%correct)
        n=int(input("Enter a 4 digit number"))
else:
    print("You quit the game")
    













