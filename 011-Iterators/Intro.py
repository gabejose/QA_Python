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

# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__()
# and __next__() to your object


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    # E.g.Stop after 20 iterations:
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            print("The iteration has stopped!")
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# StopIteration
# This statement is used to prevent an iteration from continuing forever
# In the __next__() method, we can add a terminating condition to raise an error if the iteration
# is done a specified number of times
