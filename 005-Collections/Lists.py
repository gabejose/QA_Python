# Lists
# Lists are used to store multiple items in a single variable

# To create a list:

list1 = ["apple", "banana", "orange"]
print(list1)

# List Items are ordered, changeable and allow duplicate values
# They are also indexed, with the first item having index[0], the next one has index [1] etc

# An ordered list means that the items have a defined order and it won't change
# When a new item is added, it is placed at the end of the list

# A changeable list means we can change, add and remove items in a list once it's created

# Since lists are indexed, lists can have items with the same value:
# E.g.

list2 = ["apple", "banana", "orange", "durian", "apple"]
print(list2)

# List length
# To check how many items are in a list, use the len() function:

print(len(list1))
print(len(list2))

# Data types of list items
# List items can be of any data type

list3 = [0, 1, 1, 2, 3]
list4 = [True, False, True]

# A list can also contain different data types
list5 = [True, 23, "apple", 40, False]

# type() is used to find what the data type of the list is
print(type(list2))

# You can also use the list() constructor when creating a new list
# use round brackets when using the constructor
list6 = list(("apple", "banana", "orange"))
print(list6)
