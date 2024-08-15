name = "Praveena"
print(name.lower())
print(name.upper())
print(len(name))
print(type(name))

Name = "My age is "
# Name = Name + 30 --> this is not allowed as 30 is int. u need to make it as "30" or str(30)
Name = Name + str(30)
print(Name)

how_many_planes_i_have = None
print(type(how_many_planes_i_have)) #--> NoneType
# Null is not available in Python

# id is the location used by the python interpreter.
# for same vale, python interpreter will use same id
age = 10
age2 = 10
print(id(age))
print(id(age2))