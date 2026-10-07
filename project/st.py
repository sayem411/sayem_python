# Student Portal 

serial = 1
total_credit = 0
total_point = 0
all_results = []

while True:
    print("\n--- Course", serial, "---")
    name = input("Enter Your Course Name: ")
    code = input("Enter the Course Code: ")
    credit = int(input("How Many Credits: "))

    # Attendance
    taken = int(input("Class Taken: "))
    attend = int(input("Class Attend: "))

    if attend > taken:
        print("Enter Valid Input")
        continue

    attendance = int((attend / taken) * 100)

    if attendance >= 80:
        att_marks = 7
    elif attendance >= 70:
        att_marks = 6.2
    elif attendance >= 60:
        att_marks = 6
    elif attendance >= 50:
        att_marks = 5
    elif attendance >= 41:
        att_marks = 4.2
    else:
        att_marks = 0

    # Marks
    q1 = float(input("Quiz 1: "))
    q2 = float(input("Quiz 2: "))
    q3 = float(input("Quiz 3: "))

    if q1 > 15 or q2 > 15 or q3 > 15:
        print("Enter Valid Quiz Mark")
        continue

    quiz = int((q1 + q2 + q3) / 3) + 1

    presentation = float(input("Presentation Marks: "))
    assignment = float(input("Assignment Marks: "))
    mid = float(input("Mid Marks: "))
    final = float(input("Final Marks: "))

    if presentation > 8 or assignment > 5 or mid > 25 or final > 40:
        print("Enter Valid Marks")
        continue

    total = mid + final + assignment + presentation + quiz + att_marks

    # Grade
    if total >= 80:
        grade = "A+"
        gp = 4.00
    elif total >= 75:
        grade = "A"
        gp = 3.75
    elif total >= 70:
        grade = "A-"
        gp = 3.50
    elif total >= 65:
        grade = "B+"
        gp = 3.25
    elif total >= 60:
        grade = "B"
        gp = 3.00
    elif total >= 55:
        grade = "B-"
        gp = 2.75
    elif total >= 50:
        grade = "C+"
        gp = 2.50
    elif total >= 45:
        grade = "C"
        gp = 2.25
    elif total >= 40:
        grade = "D"
        gp = 2.00
    else:
        grade = "F"
        gp = 0.00

    print("Attendance is", attendance, "%")
    print("Quiz Average:", quiz)
    print("Total:", total)

    # Save result
    all_results.append([serial, code, name, credit, grade, gp])
    total_credit += credit
    total_point += credit * gp

    serial += 1  # serial auto barbe

    again = input("Add another course? (y/n): ")
    if again != "y":
        break

# Final table
print("\nSL\tCourse Code\tCourse Title\tCredit\tGrade\tGrade Point")
for r in all_results:
    print(f"{r[0]}\t{r[1]}\t\t{r[2]}\t\t{r[3]:.2f}\t{r[4]}\t{r[5]:.2f}")

print("\nTotal Credit:", total_credit)
print("GPA:", round(total_point / total_credit, 2))