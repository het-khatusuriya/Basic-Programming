#Assignment 3# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.




from math import *

num = int(input("Enter a number:"))

print("Square root:",sqrt(num))
print("Natrual Logarithmic:",log(num))
print("Sign pof number in randian:", sin(num))


