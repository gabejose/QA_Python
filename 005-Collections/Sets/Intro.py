# Sets
# To create a set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets are used to store multiple items in a single variable
# A set is a collection which is:
# - unordered, meaning that you can't be sure which order the items will appear, they will appear in a different order and you can't
#   refer to them by index
# - unchangeable, meaning you can't change the items once the set is created. However, you can add and remove new items
# - unindexed

# Sets also can't have two items with the same value
# Duplicate values will be ignored
dupliSet = {"apple", "banana", "cherry", "apple"}
print(dupliSet)

# Use the len() method to get the number of items in a set
print(len(thisset))

# A set can be of any data type

# A set of Strings
set1 = {"apple", "banana", "cherry"}

# A set of Int
set2 = {1, 2, 3, 4, 5}

# A sert of booleans
set3 = {True, False, True}

# A set can contain items of different data types
set4 = {"abc", 26, True, 123, "jesus"}

# Sets are defined as objects with the data type 'set'
print(type(thisset))

# You can use the set() constructor to make a set
constructorSet = set(("apple", "banana", "cherry"))
print(constructorSet)
