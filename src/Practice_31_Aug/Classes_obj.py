from tkinter.font import names


class Person:
    #Attributes
    name=None
    Age=None
    Height=None

    #behaviour
    def talk(self):
        print("I can talk")

    def sleel(self, name):
        print("I can sleep")
        print("sleep", name)
    def walk(self, name):
        print("I can walk")
        print("walk", name)

#create object for the class
#ObjectRef = className()
Praveena = Person()
Praveena.name="Praveena"
print(Praveena.name)

