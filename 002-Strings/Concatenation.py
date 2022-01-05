# String Concatenation

# Use the + operator to combine two strings

a = "Good"
b = "Morning"
c = "World!"

# Add a space between the quotes to add a space between strings
d = a + " " + b + " " + c
print(d)

# To combine strings and numbers, use the format() method
# The format() method takes the passed arguments, formats them, and
# places them in a string where the placeholders {} are

age = 22
txt = "My name is Gabriel and I am {}!"
print(txt.format(age))

# Can take an unlimited number of arguments and have to be
# placed into the respective placeholders

quantity = 3
item = "cake"
price = 6
myOrder = "I want {} pieces of {} for {} pounds."
print(myOrder.format(quantity, item, price))
