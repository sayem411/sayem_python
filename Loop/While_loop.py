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
        n=n//10
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

#Guess the number
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
running = True      

print("NUMBER GUESSING GAME")
print(f"Guess number between {lowest_num} to {highest_num}")

while running:
    guess = input("Enter a number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Number is out of range!")
        elif guess < answer:
            print("Too low!! Try again")
        elif guess > answer:
            print("Too high!! Try again")
        elif guess == answer:
            print(f"CORRECT!! The answer was {answer}")
            print(f"Number of guesses needed: {guesses}")
            running = False   
    else:
        print("Invalid input! Enter a number only")
    
#guess 2 digit
#Guess the digit using while loop
import random
nump=random.randint(1,99)
n = int(input("Enter a 2 digit number: "))
while n!=0:
    num=nump
    correct=0
    while num>0:
        numc=num%10
        nc=n%10
        num=num//10
        n=n//10
        if numc==nc:
            correct+=1
    if correct==2:
        print("Congrats!You guess it right")
        break
    else:
        print("%d digit were guessed right"%correct)
        n=int(input("Enter a 2 digit number"))
else:
    print("You quit the game")













