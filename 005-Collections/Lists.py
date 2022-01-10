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

# To change the value of items within a specific range,
# define a list with the new values and refer to the range
# of index numbers where you want to insert the new values:
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Inserting more items than you replace means the new items
# will be inserted where you specify and the remaining items
# will move accordingly
list1[1:2] = ["blackcurrant", "watermelon"]
print(list1)

# Inserting less items than you replace means the new items
# will be inserted where you specified, and the remaining items
# will move accordingly

list1[1:3] = ["durian"]
print(list1)

# To insert a new list item, without replacing any of the
# existing values, use the insert() method
# The insert() method inserts an item at the specified index:

list1.insert(2, "blackberry")
print(list1)

# To add an item to the end of the list, use the append() method
list1.append("wintermelon")
print(list1)

# To append elements from another list to the current list,
# use the extend() method
# The elements will be added to the end of the list
tropical = ["mango", "pineapple", "dragonfruit"]
list1.extend(tropical)
print(list1)

# To remove a specified item, use the remove() method
list1.remove("orange")
print(list1)

# To remove an item using its index, use the pop() method
list1.pop(1)
print(list1)

# The del keyword can also remove the specified index
# as well as delete the list completely
del list1[3]

print(list1)
del list1

# To empty the list, use the clear() method
# The list will still be there, but it has no content
list2.clear()
print(list2)

# Looping through lists

# Using a for loop:
for x in thislist:
    print(x)

# Looping through lists by referring to their index number
# Use the range() and len() functions to create a suitable iterable

for i in range(len(thislist)):
    print(thislist[i])

# Using a while loop
# Use the len() function to get the length of the list,
# start at 0 and loop through the list items by referring
# to their indexes
# Increment the index by 1 after each iteration

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# List Comprehension
# Uses shorter syntax to create a new list based on the values of an existing list
# Without list comprehension you have to write a for statement with a conditional test inside

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
# newlist = [expression for item in iterable if condition == True]
# The condition is optional and can be omitted

newlist = [x for x in fruits]
print(newlist)

# Sorting Lists
# List objects have a sort() method that sorts the list alphanumerically
# ascending by default

thislist.sort()
print(thislist)

numlist = [100, 50, 22, 49, 23]
numlist.sort()
print(numlist)

# To sort into descending order, use reverse = True:

numlist.sort(reverse=True)
print(numlist)

# Customising your own sort function
# Use key = function


def myfunc(n):
    return abs(n - 50)


# Sorts the list based on how close the number is to 50
numlist.sort(key=myfunc)
print(numlist)
