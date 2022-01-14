# Joining two sets

# There are several ways to join two or more sets in Python

# One way is to use the union() method which returns a new set containing
# all items from both sets

# E.g. Using the union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Another way is to use the update() method that inserts all the items from one
# set into another
set1.update(set2)
print(set1)

# Keeping ONLY the duplicates
# The intersection_update() method keeps only the items that are present
# in both sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
print(x)

# The intersection() method returns a new set, which only contains
# the items present in both sets
# z = x.intersection(y)
# print(z)

# Keep all but NOT the duplicates
# The symmetric_difference_update() method keeps the elements that aren't present
# in both sets
# x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() method returns a new set, which only contains the elements
# that are NOT present in both sets
z = x.symmetric_difference(y)
print(z)
