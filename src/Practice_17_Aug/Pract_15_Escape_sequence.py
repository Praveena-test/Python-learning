from shlex import quote

print("Hello world")
print("Hello\nworld")
print("Hello\tworld")
print("Hello\bworld") # backward deletion

#if we have a directory in single letter like /users/n/admin,
#here to avoid we to use the r which denotes raw string
print('/users/n.txt')
print("/users/n.txt")
print(r"/users/n.txt")

#the reason we are going for double quotes instead of single quote,
#in case u want to print single quote we need must use \ before printing the single quote
print("Pravi'dear")
#print('pravi'dear') --> error will be thrown
print('pravi\'dear')