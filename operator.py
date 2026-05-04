a=5
b=2
#arithmatic operator
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#relational operator
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)
#assignment operatior
num=10;
num=num+10
print("A is:",num)
#logical ooperator
val1=True
val2=False
print("AND operator:",val1 and val2)
print("OR operator:",val1 or val2)
print("OR operator:",(a==b)or(a>b))
#logical1
num1 = 96
num2 = 99
num3 =92
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
#Logical2
#vowel/consonent
ch = 'e'
if ch =='a' or ch =='e' or ch =='i' or ch =='o' or ch =='u':
    print("Vowel")
else:
    print("Consonent")


#Ternary Operator
num1 = 20
num2 = 50
max = num1 if num1>num2 else num2
print("Maximum number =",max)