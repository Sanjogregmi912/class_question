first_subject=float(input("enter the marks of first subject \n"))
second_subject=float(input("enter the marks of second subject \n "))
third_subject=float(input("enter the marks of third subject \n"))
fourth_subject=float(input("enter the marks of fourth subject \n"))

total_marks=first_subject+second_subject+third_subject+fourth_subject
print(f"the total marks is{int(total_marks)} ")
percentage=int(total_marks/400*100)
print(f"the percentage is {percentage}%")
if percentage>=80:
    print("You have secured A+ Grade")
elif percentage >=60 and percentage <80:
    print("You have secured A Grade")
elif percentage >=40 and percentage<60:
    print("You have secured B Grade")
else:
    print("you have failed")