# Tuples are used to store multiple items in a single variable
# A collection which is ordered and unchangeable
# Written in round brackets

mytuple = ("apple", "banana", "cherry")
print(mytuple)

# Tuple Items
# Tuple items are:
# - ordered, meaning that the items have a defined order, and it won't change
# - unchangeable, meaning that once the tuple is created, we can't change, add or remove items
# - allow duplicate values, meaning that a tuple can contain items with the same value

thistuple = ("apple", "banana", "cherry", "apple", "durian")
print(thistuple)

# To find the number of items in a tuple, use the len() function:
print(len(mytuple))

# To create a tupl with only one item, you have to add a comma after the item
# If you miss it, Python won't recognize it as a tuple

anotherTuple = ("apple",)
print(type(anotherTuple))

# Data Types
# Tuple items can be of any type:

# - String
tuple1 = ("apple", "banana", "cherry")

# - Int
tuple2 = (1, 5, 7, 9, 11)

# - Boolean
tuple3 = (True, False, False)

# A tuple can also contain items of different data types
tuple4 = ("abc", 27, True, 92, "jesus")

# You can use the tuple() constructor to make a tuple

oneMoreTuple = tuple(("apple", "banana", "durian"))
print(oneMoreTuple)
