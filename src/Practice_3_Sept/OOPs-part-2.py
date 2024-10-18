#Take user input and create class

class Person:
    def __init__(self):
        self.name = input("Enter your name:\n")
        self.age = input("Enter your age:\n")
        self.phone = input("Enter your phone_number:\n")
        self.occupation = input("Enter your occupation:\n")

    def display_function(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("ph: ", self.phone)
        print("occupation: ", self.occupation)

#create object
person1 = Person()

#Call the display function
person1.display_function()