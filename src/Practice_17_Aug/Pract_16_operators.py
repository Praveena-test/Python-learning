#Operators
#assignment operator --> store right value to the left
# Unary operator --> Single operator example below,
from xmlrpc.client import boolean

negative_num= -2
print(negative_num)
#arithmetic Operator
# +,_,*,/
print(2+2)
print(2-2)
print(2*2)
print(233/2) # Quotient with decimal

# //
## %
# **
# ==
print(233//2) # Quotient will be printed without decimal
print(243%2) # remainder
# /  used for division while // provides quotient

### ** means power of
print(2**2)  # 2 to the power of 2
print(2**3) # 2 to the power of 3
print(2**4) # 2 to the power of 4

# not operator used only with boolean
Pravi_good_girl = True
print(not Pravi_good_girl) #!--> in java
# is operator specific only in python

# Relational operators also called as comparison operator
# It always returns boolean output
print("Relational operator")
print(20>40)
print(20<40)
print(30>=50)
print(30<=30)

x = 10
y = 20
print(x != y)

# Logical operator -->OR, AND and NOT
# Logical operators must be used with boolean and it will return boolean value
a = True
b = False
print(a or b)
print(a and b)

# ! and not are used in different instances
# not used where bool is used
# ! is used along with integers

# ternary operator
# If condition is true execute this line of code
# else execute this line of code
print("you can go to goa" if int(input("Enter your age: ")) > 18 else "Can't go")