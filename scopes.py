def modify_integer(x):
    x = x + 10
    print("Inside function:", x)

x = 5
print("Before function call:", x)
modify_integer(x)
print("After function call:", x)