

#Assigning Basic lambda expression to a variable
greet = lambda : print('Hello World')

#Call the lamda expression via the variable
greet()


#Use case #1 for lambda functions 
#Functions that accept other functions as parameters

def generic_numeric_operation(num1, num2, actualFunc):
    result = actualFunc(num1, num2)
    return result


def addNumbers(x , y):
    return x + y

def multiplyNumbers(x , y):
    return x * y

result = generic_numeric_operation(5, 3, addNumbers)
print ("Calling generic_numeric_operation with addNumbers")
print ("Returns : ", result)

result = generic_numeric_operation(5, 3, multiplyNumbers)
print ("Calling generic_numeric_operation with multiplyNumbers")
print ("Returns : ", result)


result = generic_numeric_operation(5, 3, lambda x, y: x + y)
print ("Calling generic_numeric_operation with lambda expression")
print ("Returns : ", result)


result = generic_numeric_operation(5, 3, lambda x, y: x * y)
print ("Calling generic_numeric_operation with lambda expression")
print ("Returns : ", result)



#Use case #2 for lambda functions 
#Functions that return other functions as result

def times(n):
    return lambda x: x * n

#Calling times() returns a lambda function that is assigned to double
double = times(2)

#We then call that lambda function through double
result = double(5)
print("Double of 5 is ", result)

result = double(3)
print("Double of 3 is ", result)

triple = times(3)
result = triple(5)
print("Triple of 5 is ", result)


