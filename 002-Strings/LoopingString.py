# Looping through a String
# We can loop through the characters in a string
# using a for loop

for x in "banana":
    print(x)

# To get the length of a string, use the len() function
a = "Good Morning World!"
print(len(a))

# To check if a certain phrase or character is present in a string,
# we can use the keyword in
# Outputs True or False

txt = "There's no such things as stupid questions, only stupid people!"
# print("stupid" in txt)

# You can also use it in an if statement
if "stupid" in txt:
    print("Yes, 'stupid' is present!")

# To check if a certain phrase or character is NOT present in a String,
# we can use the keyword not in

txt2 = "Pineapple belongs on pizza. Fight me!"
# print("anchovies" not in txt2)

# Using an if statement
if "anchovies" not in txt2:
    print("The word 'anchovies' is not present!")
