# function
def func(n,m):
    return n + m

print(func(1,4))


# Nested function in python

def outer(a, b):
    c = "saurabh"
    def inner():
        return a + b + c
    return inner()


print(outer("my", "name is "))
