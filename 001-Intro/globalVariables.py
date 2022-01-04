# Global Variables
# These are variables created outside of a function
# They can be used by everyone, both inside and outside of functions

x = "awesome!"


def myFunc():
    print("Python is " + x)


myFunc()

# Creating a variable inside a function makes it local
# This means it can only be used inside that function

print("Python is super " + x)

# To create a global variable, you can use the global keyword


def myFunc2():
    global y
    y = "annoying :("


myFunc2()

print("Java is " + y)
