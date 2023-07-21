
#function without any parameters
def greet():
    print('Hello there')
    print("Python is an awesome language")

#function with one parameter
def sayName(name):
    print(f"Hi {name}")

# function with two parameters
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum: ',sum)
    
    
# function with 3 parameters that return a result
def mult_numbers(num1, num2, num3):
    product = num1 * num2 * num3
    return product

#The function can only be called after it is defined first  
greet()    

#Calling a function and passing single string argument to it    
sayName("superman")

#Calling function and passing two number arguments to it
add_numbers(3,5)

#Calling function and passing three number arguments to it
#Storing the value returned in a variable 
result = mult_numbers(10, 5, 2)
print ("Result from calling mult_numbers is ", result)

#Function docstrings help to show the documentation of a function
#You can use the in-built help function to get documentation of an in-built function

#When the first line in the function body is a string, 
#Python will interpret it as docstring. 
# Typically this is the form of a multiline string
def cool_add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b
    
print ("Getting documentation on the function cool_add")
print (help(cool_add))

