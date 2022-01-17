# Looping Dictionaries

# Loop through a dictionary
# Use a for loop to loop through a dictionary
# The return value are the keys of the dictionary, but there are
# methods to return the values as well

# E.g. Print all key names in the dictionary, one by one:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisdict:
    print(x)

# E.g. Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)

# Use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)

# Use the items() method to loop through both keys and values
for x, y in thisdict.items():
    print(x, y)
