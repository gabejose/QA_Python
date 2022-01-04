# Numbers
# There are three numeric types in Python:
# - int
# - float
# - complex

# Like before, variables of numeric types are created when
# assigned a value

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# To verify the type of an object, use the type() function
print(type(x))
print(type(y))
print(type(z))

# Int
# A whole number, positive or negative, no decimals of unlimited length
a = 1
b = 38273736262637373
c = -123232
print(type(a))
print(type(b))
print(type(c))

# Float
# A number, positive or negative, containing one or more decimals
d = 1.10
e = 1.0
f = -35.59
g = 35e4
print(type(d))
print(type(e))
print(type(f))
print(type(g))

h = 3+5j
i = 5j
j = -5j
print(type(h))
print(type(i))
print(type(j))

# Type Conversion
# You can convert from one type to another with the int(), float() and complex() methods

k = 1
l = 2.8
m = 1j

# Convert from int to float
n = float(k)

# Convert from float to int
o = int(l)

# Convert from int to complex
p = complex(k)

print(n)
print(o)
print(p)

print(type(p))
print(type(o))
print(type(n))
