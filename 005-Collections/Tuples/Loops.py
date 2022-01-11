# Looping through a tuple

# You can loop through the tuple items using a for loop

# E.g. Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Use the range() and len() functions to loop through the tuple items by their index number

# E.g. PRint all items by referring to their index number
for i in range(len(thistuple)):
    print(thistuple[i])

# Another way is by using a while loop
# Use the len() function to get the length of the tuple
# Start at 0 and then loop through the tuple items by their index
# Increment the index by 1 after each iteration

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
