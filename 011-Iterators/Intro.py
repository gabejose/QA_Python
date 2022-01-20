# Python Iterators

# An iterator is an object that contains a countable number of values
# An iterable is an object that can be iterated upon, meaning that
# you can traverse through all the values

# Examples of iterable objects are lists, tuples, dictionaries
# and sets
# All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "Cherry"
yourit = iter(mystr)

print(next(yourit))
print(next(yourit))
print(next(yourit))
print(next(yourit))
print(next(yourit))
print(next(yourit))

# Looping through an iterator
# Use a for loop to iterate through an iterable object:
for x in mytuple:
    print(x)

for x in mystr:
    print(x)

# The for loop actually creates an iterator object and executes the next() method
# for each loop
