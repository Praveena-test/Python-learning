# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side1 = float(input("Enter the length of side-1 of the triangle that you want to classify: "))
side2 = float(input("Enter the length of side-2 of the triangle that you want to classify: "))
side3 = float(input("Enter the length of side-3 of the triangle that you want to classify: "))
if side1 == side2 and side2 == side3:
    print(f"This is a equilateral triangle")
elif side1 != side2 and side2 != side3:
    print("This is scalene")
else:
    print("This is isosceles")
