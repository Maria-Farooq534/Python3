"""
Student Grade Calculator

Input marks of 5 subjects.

Calculate percentage & grade (A, B, C…).

(Use conditionals, lists, loops).
"""

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


sub_total_marks = int(input("Enter total marks : "))
sub_obtained_marks = input(f"Enter 5 subjects marks out of {sub_total_marks}, seperated by comma : ")

# Make a list
marks = sub_obtained_marks.split(',')

# Count length of marks list. It should be 5
total_sub = len(marks)
print(f"\nTotal Subjects : {total_sub}")

obtained_marks = 0

if total_sub == 5:
    print(f"Grades and Percentage of each subject Marks:")
    for mark in marks:
        
        
        mark = int(mark)

        if mark <= sub_total_marks:

            # calculate percentage
            percentage = (mark/sub_total_marks) * 100
            # Grades
            grade = get_grade(percentage)

            print(f"{mark} marks : Grade {grade} with {percentage:.2f}% ")


            # Add marks in obtained marks
            obtained_marks += mark

        else:
            print(f"\nObtained marks {mark} should not greater than Total marks {sub_total_marks}!")

    # Overall Marks and Grades

    # Total Marks:
    total_marks = total_sub * sub_total_marks
    print(f"\nTotal Marks: {total_marks}")

    # Total Obtained Marks:
    print(f"Obtained Marks : {obtained_marks}")

    #Percentage
    total_percentage = (obtained_marks/total_marks) * 100
    print(f"Total Percentage : {total_percentage:.2f}%")

    # Overall Grade

    overall_grade = get_grade(total_percentage)
    print(f"Overall Grade : {overall_grade}")


else:
    print(f"You have enetered {len(marks)} subject marks, Please enter marks of 5 subjects.")
