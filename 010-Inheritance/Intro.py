# Inheritance

# This allows us to define a class that inherits all the methods
# and properties from another class

# Parent class is the class being inherited from (also called base class)
# Child class is the class that inherits from another class (also called derived class)

# Create a Parent Class
# Syntax is the same as creating any other class:

# E.g Create a class named Person with firstname and lastname properties
# and a printname method

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("Good Morning World! My name is " +
              self.firstname + " " + self.lastname + "!")


x = Person("Hannes", "Ocik")
x.printname()

# Create a Child class
# To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:

# E.g. Create a class named Student, which will inherit the properties and methods
# from the Person class:


class Student(Person):
    pass


x = Student("Jimmy", "Olsen")
x.printname()
