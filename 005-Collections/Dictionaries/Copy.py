# Copy Dictionaries

# There are ways to make a copy of a dictionary

# One way is to use copy() (a built - in Dictionary method)
# E.g. Use copy() to make a copy of a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = thisdict.copy()
print(mydict)

# Another way is to use the dict() function:
# E.g. Use dict() to make a copy of a dictionary
anotherdict = dict(thisdict)
print(anotherdict)
