# A variable is created the moment you
# first assign a value to it

x = 5
y = "John"
print(x)
print(y)

# Variables don't need to be declared with any particular type
# and can even change type after they have been set

x = 4  # x is of type int
x = "Jackson"  # x is now of type string
print(x)

# Casting is used to specify the data type of a variable
x = str(3)
y = int(3)
z = float(3)
print(y)
print(z)

# You can get the data type of a variable using the
# type() function

print(type(z))  # Would print float in this case

# Variable names are case sensitie
# E.g. A won't overwrite a
a = 4
A = "Hugh"
print(a)
print(A)

# Variable names can be short (x or y) or a more descriptive
# name (age, surname, total_volume)
# There are rules for python variables:
# - It must start with a letter or an underscore
# - It cannot start with a number
# - It can only contain alpha - numeric characters and underscores (A-z, 0-9 and _)
# - Are case sensitive (age, Age, AGE are different variables)

# Output Variables
# The print statement is often used to output variables
# The + character is used to combine both text and a variable
x = "awesome"
print("Python is " + x)

# Alternatively you can add a variable to another variable
x = "Python is "
y = "super awesome!"
z = x + y
print(z)
