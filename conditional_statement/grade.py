marks=int(input("Enter student marks:"))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("The grade is:",grade)

#grade
marks = 89
if marks>=80:
    print("A+")

elif marks>=70:
    print("A")

elif marks>=60:
    print("A-")

elif marks>=50:
    print("B")

elif marks>=40:
    print("c")

elif marks>=33:
    print("D")

else:
    print("Fail")