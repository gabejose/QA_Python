# Slicing strings
# You can return a range of characters by using the slice syntax

# Specify the start and end index, separated by a colon
# Returns a part of the string

a = "Good Morning World"
print(a[2:5])

# Slicing from the start
# By leaving out the start index, the range will start at the first
# character

print(a[:5])  # Get the characters from the start to (not including) position 5

# Slicing to the end
# By leaving out the end index, the range will go to the end

print(a[2:])  # Get the characters from position 2 all the way to the end

# Negative Indexing
# Use negative indexes to start the slice from the end of the string

b = "Hello World!"
# Get the characters from "o" in "World!" (position -5) to (but not included:) "d" in "World!" (position -2)
print(b[-5:-2])
