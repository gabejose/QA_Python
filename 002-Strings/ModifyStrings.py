# Modifying Strings

# To return a string in upper case, use the upper() method

a = "Good Morning World!"
print(a.upper())

# To return a string in lower case, use the lower() method

print(a.lower())

# Whitespace is the space before and/or after the actual text
# You want to remove the whitespace very often
# The strip() method removes any whitespace in the text

print(a.strip())

# To replace a string with another string, use the replace() method
# replace("[part to replace goes here]", "[what you want it to be replaced with goes here]")
print(a.replace("Good", "Bad"))

# Split string
# Returns a list where the text between the specified separatro becomes the list items
b = "Hello, World!"
print(b.split(","))  # returns ['Hello', 'World!']
