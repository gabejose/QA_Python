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

# Accessing list items
# To access them, refer to the index number
print(list1[1])  # returns banana

# Negative indexing means starting the from the end
# -1 refers to the last item, -2 refers to the second last item etc

print(list1[-1])  # returns orange

# Range of indexes
# You can specify a range of indexes by specifying where to start and where to end the range
# Returns a new list with the specified items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# The search starts at index 2 and end at (but not including) index 5
print(thislist[2:5])

# Returns items from the beginning to (not including) "kiwi"
print(thislist[:4])

# Returns items from "cherry" to the end
print(thislist[2:])

# Check if an item exists
# Use the in keyword

if "apple" in list1:
    print("There is an apple in the list!")

# To change the value of a specific item, refer to the index number:
list1[1] = "blackcurrant"
print(list1)
