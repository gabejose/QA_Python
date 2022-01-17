# Access Dictionary Items

# You can access the items of a dictionary by referring
# to its key name, inside square brackets

# E.g. Get the value of the "model" key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]
print(x)

# You can also use the get() method to give you the same result
y = thisdict.get("brand")
print(y)

# Get keys
# The keys() method will return a list of all the keys in the dictionary

# E.g. Get a list of the keys
x = thisdict.keys()
print(x)

# E.g. Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)  # Before the change

car["color"] = "white"
print(x)  # After the change

# Get values
# The values() method returns a list of all the values in the dictionary
x = thisdict.values()
print(x)

# The list of the values is a view of the dictionary, meaning that any changes done
# to the dictionary will be reflected in the values list

# E.g. Make a change in the original dictionary, and see that the valyes list
# gets updated as well:
x = car.values()
print(x)  # Before the change

car["year"] = 2022
print(x)  # After the change

# Get Items
# The items() method returns each item in a dictionary, as tuples in a list

x = thisdict.items()
print(x)

# Check if key exists
# Use the in keyword to determine if a specified key is present in a dictionary

if "model" in thisdict:
    print("Yes! model is one of the keys!")
