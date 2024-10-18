def my_fun(a,b,c=10):
    print(a,b,c)

#my_fun(10, b=20, 30) #SyntaxError: positional argument follows keyword argument
my_fun(10, 20)