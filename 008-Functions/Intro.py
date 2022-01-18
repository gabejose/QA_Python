# Functions in Python

# To create a function, use the def keyword:
def myFunction():
    print("Good Morning World!")


# To call a function, use the function name followed by parenthesis:
myFunction()

# Arguments
# Information can be passed into functions as arguments

# Arguments are specified after the function name, inside the parentheses
# You can add as many arguments as you wish, just separate them with a comma


def my_function(fname):
    print("Good morning " + fname + "!")


my_function("Jesus")

# A function must be called with the correct number of arguments
# If the function expects 2 arguments, you have to call the function with 2 arguments

# E.g. A function that expects 2 arguments


def this_function(fname, lname):
    print("Good morning " + fname + " " + lname + "!")


this_function("Reece", "Elder")

# Arbitrary Arguments, *args
# If you don't know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition
# The function will receive a tuple of arguments, and can access the items accordingly:

# E.g.


def that_function(*kids):
    print("The youngest child is " + kids[2])


that_function("Jackson", "Tobias", "Jeffrey")

# Keyword Arguments
# You can also send arguments with the key = value syntax
# This way, the order of the arguments does not matter


def more_function(child3, child2, child1):
    print("The youngest child is " + child3)


more_function(child1="Jesus", child2="Joe", child3="James")

# Arbitrary Keyword Arguments, **kwargs
# If you don't know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition

# This way the function will receive a dictionary of arguments, and can access the items
# accordingly:

# E.g. If the number of keyword arguments is unknown, add a double ** before the parameter name:


def a_function(**kid):
    print("His last name is " + kid["lname"])


a_function(fname="Boris", lname="Johnson")

# Default Parameter Value
# If we call the function without argument, it uses the default value:


def default_function(country="Norway"):
    print("I am from " + country)


default_function("Sweden")
default_function("Singapore")
default_function("Poland")
default_function()

# Passing a list as an argument
# You can send any data types of argument to a function and it will
# be treated as the same data type inside the function

# E.g. If you send a list as an argument, it will still be a list when it reaches the function:


def food_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
food_function(fruits)

# Return values
# Use the return statement to let a function return a value


def return_function(x):
    return 5 * x


print(return_function(3))
print(return_function(25))
print(return_function(123))

# Recursion
# A common mathematical and programming concept, meaning that a function
# can call itself.
# This has the benefit of meaning that you can loop through data to reach a result


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
