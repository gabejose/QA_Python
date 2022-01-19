# Classes and Objects in Python

# To create a class, use the keyword class:
class MyClass:
    x = 5


# Now we can use the class named MyClass to create objects:
p1 = MyClass()
print(p1.x)

# The _init_() function
# Use this function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:

# E.g. Create a class named Person, use the __init__() function to assign values for name and age:


class Person:
    def __init__(randomObject, name, age):
        randomObject.name = name
        randomObject.age = age

    def myfunc(sjw):
        print("Hi there! My name is " + sjw.name)


p1 = Person("Jackson", 23)
p1.myfunc()

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object

# The self parameter
# This is a reference to the current instance of the class, and is used to access
# variables that belong to the class
# Doesn't have to be named self, but it has to be the first parameter of any function in the class

# Modify Object Properties
# E.g Set the age of p1 to 40:
p1.age = 40

# Delete Object Properties
# E.g. Delete the age property from the p1 object
del p1.age

# Delete Objects
# E.g. Delete the p1 object
del p1

# The pass statement
# Because class definitions can't be empty, use the pass statement to avoid getting an error

# class Person:
#   pass
