

#Function with one default parameter
def greet(name, message='Hello'):
    print (f"{message} {name}")


#Call function with one argument, it uses the default parameter
greet("Superman")

#Call function with 2 arguments, the 2nd argument replaces the default parameter
greet("Superman","Goodbye")


#Function with two default parameters
def add_numbers(a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(2)

# function call with no arguments
add_numbers()




def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

#Arguments are always passed to parameters based on the parameter positioning
display_info("Peter", "Parker")


#To pass arguments in an order different from parameter position, use keyword arguments
display_info(last_name = 'Cartman', first_name = 'Eric')

#If you want to mix and match positional and keyword arguments,
#positional arguments must come first

display_info('Bruce', last_name = 'Banner')


#Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.
#Otherwise, the compiler will flag an error

#Uncomment this to see the error
#display_info(first_name = 'Tony', 'Stark')

display_info(first_name = 'Tony', last_name = 'Stark')
