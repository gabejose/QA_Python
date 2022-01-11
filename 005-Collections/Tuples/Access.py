# Accessing tuple items

# Refer to the index number inside square brackets

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "durian")
print(thistuple[1])

# Negative indexes start from the end
# -1 is the last item, -2 is the second to last item etc

print(thistuple[-1])

# Range of indexes
# You can specify a range of indexes by specifying where to start and end the range
# When doing this, a new tuple with the specified items is returned

# Returns the third, fourth and fifth item
# Search starts at index 2 and ends at (but not included) index 5
print(thistuple[2:5])

# Leaving out the start value means the range will start from the first item:
print(thistuple[:4])

# Leaving out the end value, the range will continue to the end of the list
print(thistuple[2:])

# To check if an item is present in a tuple, use the in keyword
if "apple" in thistuple:
    print("Yes, there is an apple in this tuple!")
