# Scope
# A variable is only available from inside the region it is created

# Global variables are available from within any scope, gloabl and local
x = 300


def myfunc():
    # A variable created inside a function belongs to the local scope of that function
    # and can only be used inside that function

    # Here the variable x isn't available outside the function,
    # but it is available for any function inside the myfunc() function

    print(x)

    # def myinnerfunc():
    #    print(x)
    # myinnerfunc()


myfunc()

print(x)
