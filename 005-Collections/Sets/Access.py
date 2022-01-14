# Accessing Set Items

# Because you can't access items in a set by referring to its index,
# you have to loop through the set using a for loop, or using the
# in keyword to check for a specific value

# E.g. Loop through the set and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# E.g. Check if "banana" is present in this set
# Will output either True or False (True in this case)
print("banana" in thisset)
