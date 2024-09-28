def letter_grade(average_grade):
    if average_grade >= 90:
        grade = 'A'
    elif average_grade >= 80:
        grade = 'B'
    elif average_grade >= 70:
        grade = 'C'
    elif average_grade >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def main():
    student_name = input("What is your name? \n")

    grades = [
        float(input("What is your first grade? \n")),
        float(input("What is your second grade? \n")),
        float(input("What is your third grade? \n")),
        float(input("What is your fourth grade? \n")),
        float(input("What is your fifth grade? \n")),
    ]


    average = sum(grades) / len(grades)
    print("Your name is: ", student_name)
    print("Your average grade is ", average)
    print("Your letter grade is: ", letter_grade(average))

main()

