#Assignment 5

# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.


studentdetails = {"Het":97,"Dhvani":96,"Raj":90}
studentname = str(input("Please Enter Student name:"))
if studentname in studentdetails:
    print("Marks of {} is: ".format(studentname),studentdetails[studentname])
else:
    print("Student name not found in records")