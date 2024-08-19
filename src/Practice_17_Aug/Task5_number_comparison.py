### Task #5
"""
Create a program that takes two numbers as input and prints whether the first number is
greater than, less than, or equal to the second number.
"""

num1=float(input("Enter the First number: "))
num2=float(input("Enter the Second number: "))

if num1>num2:
    print("First number ", num1, "is greater than second number",num2)
elif num2>num1:
    print("First number ", num1, "is lesser than second number",num2)
else:
    print("First number ", num1, "is equal to Second number ", num2)