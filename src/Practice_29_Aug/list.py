
my_list=[1,2,3]
print(my_list)
for element in my_list:
    print(element)
#range is also list, so in the for loop instead of range we have used the my_list here

#overwriting the index 0--> 1 with Pravi
my_list[0]="Pravi"
print(my_list)
# print(my_list[10]) #list index out of range

#appending --> to add only one value to the end of the list
my_list.append(4)
my_list.append(4)
my_list.append(4)
my_list.append(4)
print(my_list)

# to add multiple values to the end of the list, we need to use extend
my_list.extend([9,7,8,4,3,1])
print(my_list)

#Single value can also be added using extend
my_list.extend([10])
print(my_list)
print(len(my_list))
#insert --> used for inserting in the middle and shift the other values by index of 1
my_list.insert(1,"good")#['Pravi', 'good', 2, 3, 4, 4, 4, 4, 9, 7, 8, 4, 3, 1, 10]
print(my_list)
print(len(my_list))

# -negative index can be used
my_list.insert(-1,"good") # ['Pravi', 'good', 2, 3, 4, 4, 4, 4, 9, 7, 8, 4, 3, 1, 'good', 10]
print(my_list)
print(len(my_list))

#remove
my_list.remove("Pravi")
print(my_list)

#copy list
my_copy_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_copy_list)
#print(my_copy_list.sort(reverse=False)) #not supported between instances of 'int' and 'str'
#sorting --> need to remove the strings
#sort
#reverse shall be used

#concatenation
l1 = [1,2,3]
l2 = [4.5,6]
l3 = l1+l2

print(l3)

#pop will remove the last item in the list
print(l3.pop())
print(l3)
print(l3.pop(0))
print(l3)

#list is mutable in nature, meaning the values can be reassigned and changed mutable means changeable
