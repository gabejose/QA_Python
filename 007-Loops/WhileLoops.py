# While Loops

# The while loop can execute a set of statements
# as long as a condition is true
# Remember to increment i, otherwise the loop will never stop

# E.g. Print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1

# The continue statement
# With the continue statement we can stop the current iteration
# and continue with the next:

# E.g. Continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Else statement
# With the else statement, we can run a block of code once when the condition
# no longer is true:

# E.g. Print a message once the condition is false:
i = 1
while i > 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
