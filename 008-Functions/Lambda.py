# Lambda

# A lambda function is a small anonymous function
# Can take any number of arguments, but can only have one expression

# Syntax
# lambda arguments : expression

# E.g. Add 10 to argument a, and return the result:
def x(a): return a + 10


print(x(5))

# Lambda function can take any number of arguments
# E.g. Multiply argument a with argument b and return the result:


def x(a, b): return a * b


print(x(5, 6))

# E.g. Summarise argument a, b and c and return the result:


def x(a, b, c): return a + b + c


print(x(5, 6, 27))

# Why use lambda functions?

# E.g. You have a function definition that takes one argument, and that argument
# will be multiplied with an unknown number:


def myfunc(n):
    return lambda a: a * n


# Use that function definition to make a function that always doubles the number you send in:
mydoubler = myfunc(2)

print(mydoubler(11))

# Alternatively, you can use the same function to make a function that always triples the number you send in:
mytripler = myfunc(3)

print(mytripler(11))
