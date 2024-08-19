### Task #3
"""
Explain the difference between the = operator and the == operator in Python.
--> The = Operator is assignment operator is used to assign the value of right to left
--> The == operator is relative operator used to compare whether given two values are equal.
    It returns Boolean output (i.e) True or False.
"""
# Example of = operator
Name = "Praveena"
Age = 30
Employment_details=input("Enter employment status: ")
print(Name,Age,Employment_details)
print("Thus the assignment operator is used to assign the value of right to left as per the above example")

num1, num2 =10, 10
if num1==num2:
    print(num1, "is equal to ", num2)

print("== operator is used to compare and tell if the both the variables are same or not")

"""
- What does the ** operator do in Python, and how is it used?
"""
# ** operator is an Arithmetic operator used to compute the power values.
# (i.e) 45**3 ==> implies 45*45*45
# example on how to use it below,
Num=int(input("Enter integer number to compute the power of 5 of the given number: "))
print("The result of Num power 5 is: ", Num**5 )

"""
- What does the ^ operator do in Python, and in what context is it commonly used?
"""
# The ^ operator is bitwise NOR operator.
A=  10
a = 20
Xor = A ^ a
print("XOR of A and a is: ", Xor)