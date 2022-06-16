"""
Program: gpa_evaluator.py
Author: Matt Kimmel
Last date modified: 06/16/2022

The purpose of this program is to prompt the user for input
about a student including their name and GPA to determine
whether they qualify for either the Dean's List or the Honor
Roll. 
"""
print("GPA Evaluator\n")
print("Enter student information to determine if a student qualifies for the Dean's List or the Honor Roll\n")
last_name = input("Please enter the student's last name or enter 'ZZZ' to exit: ")

if last_name == "ZZZ":
    quit()

first_name = input("Please enter the student's first name: ")
gpa = float(input("Please enter the studen't GPA: "))

if gpa >= 3.5:
    print(f"{first_name} {last_name} has qualified for the Dean's List")

elif gpa >= 3.25:
    print(f"{first_name} {last_name} has qualified for the Honor Roll")

else:
    print(f"{first_name} {last_name} does not qualify for either the Honor Roll or Dean's List")

input()
