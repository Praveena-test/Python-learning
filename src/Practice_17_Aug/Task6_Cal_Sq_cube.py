# Python program to calculate square and cube of the number given by user
num= float(input("Enter the number to calculate square & cube:"))
print("Square of ", num, "is ", (num**2))
print("Cube of ", num,"is ", (num**3))

#Printing using format function
print("Square of", num, ":", f"{num**2:.3f}")
print("Cube of ", num, f"{num**3:.3f}")