# Changing tuple values

# Once a tuple is created, you can't change the values

# One way to work around this is to convert the tuple into a list, change the list
# and convert it back into a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Similarly, to add items to a tuple, convert the tuple into a list etc

# E.g. Add "orange" to the tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Another way is to create a new tuple with the item(s) and add that to the existing tuple:
y = ("strawberry",)
thistuple += y
print(thistuple)

# To remove items, you can use the same workaround method

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# You could also delete the tuple completely:
del thistuple
print(thistuple)  # Outputs an error as it no longer exists
