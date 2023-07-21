#Variadic args parameters are used when it is
#not known in advance how many arguments a function
#might receive.
#It allows a variable number of arguments to be 
#passed which are all stored in a tuple

def add(*args):
    print (type(args))
    total = 0
    for arg in args:
        total += arg
    return total


result = add(10,20,30)
print (result)

result = add(10,20,30,40,50)
print (result)

#It is ok to add a variadic args parameter
#after standard positional arguments 

def add_second(x, y, *args):
    print (f"x is {x}, y is {y}")
    print (f"args is {args}")
    
    
add_second(10,20,30,40,50)


#If you want to add standard positional arguments 
# after a variadic args parameter
# you must provide it using a keyword argument

def add_third(x, y, *args, z):
    print (f"x is {x}, y is {y}")
    print (f"args is {args}")
    print (f"z is {z}")

#if uncomment below and run, you will get error
#add_third(10,20,30,40,50)

add_third(10,20,30,40, z = 50)


def showVals(x, y, z):
    return f" {x} , {y}, {z} "

#You can call a function which has multiple parameters
#by unpacking a list or tuple

myvals = [1, 3 ,5]
print(showVals(myvals[0], myvals[1], myvals[2]))

#If you wish to use all the values in a list / tuple
#as arguments to parameters of a function, a shortcut
#is to unpack the list / tuple
print(showVals(*myvals))


