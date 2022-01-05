# Booleans represent one of two values: True or False

# When comparing two values, the expression is evaluated
# and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# The bool() function allows you to evaluate any value
# Will give True or False in return

print(bool("Hello"))
print(bool(15))

# Almost any value is evaluated to True if it has some sort of content
# Any string is true, except empty strings
# Any number is true, except 0
# Any list, tuple, set and dictionary are true, except empty ones

bool(123)
bool(["apple", "banana", "orange"])

# Functions returning a Boolean


def myFunc():
    return True


if myFunc():
    print("AWESOME!")
else:
    print("aw that sucks")

# The isinstance() function can be used to determine if an object
# is of a certain data type

x = 200
print(isinstance(x, int))
