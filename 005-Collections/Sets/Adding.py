# Adding Set Items

# Once a set is created, you cannot change its items
# You can however add new items

# To add an item to a set, use the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)

# To add items from another set into the current set,
# use the update() method

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add any iterable
# The object in the update() method doesn't have to be a set,
# it can be any iterable object (tuples, lists, dictionaries, etc)

# E.g. Add elements of a list to at set:
mylist = ["kiwi", "durian"]
thisset.update(mylist)
print(thisset)
