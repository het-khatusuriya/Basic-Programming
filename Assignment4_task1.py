#Assignment 4
# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.


try:
    file = open('assignment4_textfile.txt')
    print("Line-1:",file.readline())
    print("Line-2:",file.readline())
    print("Line-3:",file.readline())
    file.close()
    
except FileNotFoundError:
    print("file 'assignment4_textfile.txt' not found over that place")
    
    
    
    
    
