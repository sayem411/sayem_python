
#1. Num Classify: 8 → Positive | -5 → Negative
number=int(input("Enter Number:"))
if(number>0):
    print("Positive")
else:
    print("Negative")

#2. Even/Odd: 11 → Odd | 6 → Even
number1=int(input("Enter Number1: "))
if(number1%2==0):
    print("Even")
else:
    print("Odd")

#3.    Max of 2: 5, 9 → 9 | 7, 7 → Equal
num1=int(input("Enter Number1: "))
num2=int(input("Enter Number2: "))
if(num1>num2):
    print("Max=",num1)
elif(num1<num2):
    print("Max=",num2)
else:
    print("Equal")

#4.    Max of 3: 4, 9, 6 → 9
num1=int(input("Enter Number1: "))
num2=int(input("Enter Number2: "))
num3=int(input("Enter Number1: "))
if(num1>num2 and num1>num3):
    print("Max=",num1)
elif(num2<num1 and num2<num3):
    print("Max=",num2)
else:
    print("Max=",num3)
#5.    Grading: 85 → A | 30 → Fail

#6.    Leap Year: 2024 → Leap Year | 2023 → Not

#7.    Divisibility: 55 → Divisible (by 5 & 11)

#8.    Vowel/Consonant: a → Vowel | b → Consonant

#9.    Case Detect: A → Uppercase | z → Lowercase

#10.    Profit/Loss: CP 100, SP 120 → Profit

#11.    Temp Class: 35 → Hot | 25 → Cold

#12.    Electricity Bill: 120 units → 700
#(First 100 units → 5 taka/unit
#Next units → 10 taka/unit)

#13.    Triangle Valid: 3, 4, 5 → Valid | 1, 2, 10 → Invalid

#14.    Calculator: 5 + 3 → 8 | 10 - 2 → 8

#15.    Pass/Fail: Marks 60, Atten. 60% → Fail (Req. 40 & 75%)
