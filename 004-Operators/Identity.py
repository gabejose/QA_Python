# Identity Operators

# Used to compare objects if they are the same

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# is - Returns true if both variables are the same object

# Returns True as z is the same object as x
print(x is z)

# Returns False becuase x is not the same object as y
# despite having the same content
print(x is y)

# == and 'is' aren't the same (see below)
# Returns true because x is equal to y
print(x == y)

# is not - Returns true if both variables aren't the same object

# Returns false as z is the same object as x
print(x is not z)

# Returns true because x is not the same object as y
# despite having the same content
print(x is not y)

# != and 'is not' aren't the same
# Returns false because x is equal to y
print(x != y)
