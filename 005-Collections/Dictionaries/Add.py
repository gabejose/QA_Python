# Add Dictionary Items

# Adding an item to the dictionary is done by using a new index key
# and assigning a value to it:

# E.g
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["color"] = "red"
print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument
# If the item doesn't exist, the item will be added
# The argument must be a dictionary, or an iterable object with key:value pairs

# E.g. Add a colour item to the dictionary by using the update() method
thisdict.update({"color": "purple"})
print(thisdict)
