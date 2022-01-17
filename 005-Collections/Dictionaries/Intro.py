# Dictionary
# Used to store data in key:value pairs

# A dictionary is a collection which is:
# - ordered (3.6 and earlier, dictionaries weren't ordered)
# - changeable, meaning that we can add, remove or change items after the dictionary is created
# - no duplicates, meaning that dictionaries cannot have 2 items with the same key

# Dictionaries are written with curly brackets, and have keys and values:
# E.g. Create and print a dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

# Dictionary Items
# The items are presented in key:valye pairs
# They can be referred to by using the key name

# E.g. Print the "brand" value of the dictionary:
print(thisdict["brand"])

# Duplicates not allowed

# E.g. Duplicate values will overwrite existing values:
thatdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2022
}

print(thatdict)

# To get the number of items a dictionary has, use the len() function:
print(len(thisdict))

# The values in dictionary items can be of any data type:

anotherdict = {
    "brand": "Ford",  # string
    "electric": False,  # boolean
    "year": 1964,  # int
    "colors": ["red", "white", "blue"]  # list
}

# Dictionaries are defined as objects with the data type 'dict' <class 'dict'>
print(type(anotherdict))
