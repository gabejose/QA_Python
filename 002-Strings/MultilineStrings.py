# Multiline Strings
# You can assign a multiline string to a variable by using
# three single or quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(b)

# Strings in Python are arrays of bytes representing unicode
# characters
# However, there is no character data type, so a single character
# is a string of length 1
# Square bracekts can be used to access elements of the string

c = "Good Mornng World!"
print(c[1])
