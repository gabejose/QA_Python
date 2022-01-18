# Conditionals and If statements in Python

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# An if statement is written by using the if keyword
a = 33
b = 200

if b > a:
    # Indentation is important to define scope in the code (equivalent of curly brackets in other languages)
    print("b is greater than a!")

# Elif
# Python's version of else if
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
# The else keyword catches anything that isn't caught by the preceding conditions

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b!")

# Short hand If
# If you only have one statement to execute, you can put it on the same line
# as the if statement

# E.g. One line if statement:
if a > b:
    print("a is greater than b")

# Short hand If ... Else
# E.g. One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

# You can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
# The 'and' keyword is a logical operator and is used to combine conditional statements:

# E.g. Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true!")

# Or
# The 'or' keyword is a logical operator, and is used to combine conditional statements:

# E.g. Test is a is greater than b, OR if a is greater than c
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True!")

# Nested If
# You can have if statements inside if statements
# This is called nested if statements

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass statement
# If statements cannot be empty, but if for some reason have an if statement
# with no content, put in the pass statement to avoid getting an error
a = 33
b = 200

if b > a:
    pass
