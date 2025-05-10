#Assignment 4

# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

file = open("assignment4_textfile.txt",'r')
print("file content till now: \n",file.read())

file = open("assignment4_textfile.txt",'a')
userinput= input("Please enter input to add in a file:")
appendingtext = file.write(userinput)

file = open("assignment4_textfile.txt",'r')
print("file content after append opeartion: \n",file.read())