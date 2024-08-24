# max of three numbers


n1 = 10000
n2 = 10000
n3 = 89

if n2 < n1 >n3:
    print(" first max is ", n1)
elif n1 == n2 == n3:
    print(" All numbers are same number ", n1)
elif n2 > n3:
    print("second Max is", n2)
# below code is not executed because 10000>89 and interpreter exits after the above condition.
# Even though n1 == n2, it doesn't get executed.
# elif n2 == n3:
#     print(" N2 and N3 numbers are same numbers ", n2)
# elif n1 == n2:
#     print(" N1 and N2 numbers are same numbers ", n2)
else:
    print(" else stmt Max is", n3)

# Alternately we can also use max function
# print(f"Max number is: {max(n1, n2, n3)}")