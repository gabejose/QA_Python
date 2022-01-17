# Remove Dictionary Items

# There are several methods to remove items from a dictionary:

# pop()
# The pop() method removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# thisdict.pop("model")
print(thisdict)

# popitem()
# The popitem() method removes the last inserted item (before Python 3.7, a random item
# is removed instead):
thisdict.popitem()
print(thisdict)

# del
# The del keyword removes the item with the specified key name:
# Can also be used to delete the dictionary completely:
del thisdict["model"]

# clear()
# The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)
