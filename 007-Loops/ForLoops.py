# For loops

# A for loop is used for iterating over a sequence (either a list, tuple
# dictionary, set or a string)

# With the for loop we can execute a set of statements, once for each item
# in a list, tuple, set etc

# E.g. Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The for loops doesn't require an indexing variable to set beforehand

# Looping through a string
for x in "banana":
    print(x)

# The break statement
# With the break statement, we can stop the loop before it has looped
# through all the items:

# E.g. Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# E.g. Exit the loop when x is "banana", but the break comes before the print
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue statement
# With the continue statement, we can stop the current iteration of the loop
# and continue with the next:

# E.g. Do not print banana
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() function
# Use the range() function to loop through a set of code a specific number
# of times
# Returns a sequence of numbers, starting from 0 by default, and increments by 1
# (by default) and ends at a specified number

# E.g. Using the range() function:
for x in range(6):
    print(x)

# You can specify the starting value in the range() function by adding
# a parameter: range(2, 6)
# This means values from 2 to (but not including) 6

# E.g. Using the start parameter:
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1
# It is possible to specify the increment value by adding a third parameter:
# range(2, 30, 3)

# E.g. Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed
# when the loop is finished:

# E.g. Print all numbers from 0 to 5, then print a message when the loop has ended
for x in range(6):
    print(x)
else:
    print("Loop has finished!")

# Nested Loops
# The inner loop will be executed one time for each iteration
# of the "outer loop":

# E.g. Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
for x in adj:
    for y in fruits:
        print(x, y)

# The pass statement
# for loops can't be empty, but if you have a for loop with no content,
# put in the pass statement to avoid getting an error

for x in [0, 1, 2]:
    pass
