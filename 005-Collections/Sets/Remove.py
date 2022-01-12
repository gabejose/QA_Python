# Removing Set Items

# To remove an item in a set, use the remove() or the discard()
# method

# E.g. Remove "banana" by using the remove() method
thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")

print(thisset)

# E.g. Remove "apple" by using the discard() method
# thisset.discard("apple")
# print(thisset)

# The pop() method also works, but it removes the last item
# However, because sets are unordered, you won't know what item is removed

# x = thisset.pop()
# print(thisset)

# The clear() method empties the set

thisset.clear()
print(thisset)

# The del() deletes the set completely
del thisset
print(thisset)  # Outputs an error as it doesn't exist
