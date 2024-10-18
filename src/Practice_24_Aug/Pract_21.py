# Range function
# range(10) --> 10 corresponds to the end value
# range(1, 10) --> 1 is the start value and 10 is the end value
# range(1, 10, 2) --> 1 is the start value and 10 is the end value and 2 is the increment size
#example pblms
print(list(range(20)))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(10,20))) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(10,20, 2))) #[10, 12, 14, 16, 18]

# print odd number b.w 1 to 10
print(list(range(1, 10, 2))) #[1, 3, 5, 7, 9]

#print even number between 2 to 10
print(list(range(4, 10, 2))) #[4, 6, 8]

#print even number between 2 to 10 in reverse order
print(list(range(10, 2, -2))) #[10, 8, 6, 4]

#negative number can also be start and end values
print(list(range(-10, -1, 3))) #[-10, -7, -4]

print(list(range(-10, -1, -3 )))  #[]
# no output will be printed as the first itself will be -10-3 = 13 and it is not accordance with the end value.



