# Nested Dictionaries

# A dictionary can contain dictionaries, this is called nested dictionaries

# E.g. Create a dictionary that contain three dictionaries:
myfamily = {
    "child1": {
        "name": "Jackson",
        "year": 2004
    },

    "child2": {
        "name": "Jesus",
        "year": 33
    },

    "child3": {
        "name": "Boris",
        "year": 1982
    }
}

print(myfamily)

# Alternatively, you can add three dictionaries into a new dictionary:

# E.g. Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name": "Jackson",
    "year": 2004
}

child2 = {
    "name": "Jesus",
    "year": 33
}

child3 = {
    "name": "Boris",
    "year": 1982
}

anotherfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(anotherfamily)
