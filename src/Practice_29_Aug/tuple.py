#tuple is also collection of item but replacing values in a particular index is not possible
from src.Practice_29_Aug.list import my_list, my_copy_list

my_tuple=(1,2,3,4,5)
#my_tuple[3]=64 #TypeError: 'tuple' object does not support item assignment
print(my_tuple)

#tuple is used where the collection of item can not be changed

#conversion between list and tuple is possible
my_tuple=list(my_copy_list)
print(my_tuple)
my_converted_tuple=tuple(my_tuple)