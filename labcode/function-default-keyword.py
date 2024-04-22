

#Function with one default parameter
def greet(name, message='Hello'):
    print (f"{message} {name}")


print ("\nCalling function greet with a single value Superman")
#Call function with one argument, it uses the default parameter
greet("Superman")

print ("\nCalling function greet with two values: Superman and Goodbye")
#Call function with 2 arguments, the 2nd argument replaces the default parameter
greet("Superman","Goodbye")


#Function with two default parameters
def add_numbers(a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


print ("\nCalling function add_numbers with two values: 2 and 3")
# function call with two arguments
add_numbers(2, 3)

print ("\nCalling function add_numbers with one value: 2")
#  function call with one argument
add_numbers(2)

print ("\nCalling function add_numbers without passing any values")
# function call with no arguments
add_numbers()




def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

print ("\nCalling display_info in the normal manner")
#Arguments are always passed to parameters based on the parameter positioning
display_info("Peter", "Parker")


print ("\nCalling display_info with positional parameters")
#To pass arguments in an order different from parameter position, use keyword arguments
display_info(last_name = 'Cartman', first_name = 'Eric')

print ("\nCalling display_info with mix and match positional and keyword")
#If you want to mix and match positional and keyword arguments,
#positional arguments must come first
display_info('Bruce', last_name = 'Banner')


#Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.
#Otherwise, the compiler will flag an error

#Uncomment this to see the error
#display_info(first_name = 'Tony', 'Stark')
print ("\nDemo that keyword arguments must be used for all remaining arguments")
display_info(first_name = 'Tony', last_name = 'Stark')
