# Unpacking a tuple
# Assigning values to a tuple is known as "packing" a tuple:

fruits = ("apple", "banana", "cherry")

# In python, we can extract the values back into variables
# This is called "unpacking"

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# The number of variables must match the number of values in the tuple
# Otherwise, you must use an asterisk to collect the remaining values as a list

# Using Asterisk *
# You can add an * to the variable name and the values will be assigned to the variable as a list:

# E.g. Assign the rest of the values as a list called "red"
moreFruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = moreFruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python assigns valyes
# to the variable until the number of values left matches the number of variables left

# E.g. Add a list of values the "tropic" variable:

evenMoreFruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = evenMoreFruits

print(green)
print(tropic)
print(red)
