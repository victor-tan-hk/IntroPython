#String type
hisname = "Superman"
#The type function tells us the type/class of a variable
print(hisname, 'is of type', type(hisname))

#Strings can be delimited by either single or double quotes
hername = 'Wonder Woman'
print(hername, 'is of type', type(hername))

#Number types are either integer, floating point or complex
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.345
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))

print("When designating binary, octal or hexademical values, prefix the values with 0b, 0o or 0X")
print ("All numbers will be printed out in their corresponding decimal value")
print(0b1101011)  # prints 107

print(0xFB + 0b10)  # prints 253

print(0o15)  # prints 13 

print ("Large numbers can be specified with underscores to make them easier to read")
print ("They will however be printed without the underscores")
count = 10_000_000_000
print("The value of count is ", count)


print ("Boolean variables are either True or False")
#Can be used in conditional expressions in if-else
is_employee = True
is_manager = False
print (type(is_employee));
print (type(is_manager));

#We use the bool function to determine whether the value of a variable is 
#interpreted as true or false

print("Using bool function to check on the value of variables holding boolean values")
print(bool(is_employee))
print(bool(is_manager))


print("Checking on the value of variables holding non-boolean values")
# These variables can also be used in conditional expression in if-else

# A non empty string is considered true
print(bool('Hi'))
# An empty string is considered false
print(bool(''))

# Any number other than 0 is considered true
print(bool(100))
print(bool(-50))

# zero is considered to be false
print(bool(0))


print ("Using the isinstance function to check whether a particular variable is of a specific data type")
print ("Checking this variable value to see whether it is a string or integer data type: ", hisname)
print(isinstance(hisname, int))
print(isinstance(hisname, str))
print ("Checking this variable value to see whether it is a string or integer data type: ", num1)
print(isinstance(num1, int))
print(isinstance(num1, str))


print ("Python is a dynamically typed language")
print ("You can assign values (which are actually objects) of different types to the same variable")
message = 'Hello';
print (type(message))
message = 100
print (type(message))
message = 3.96
print (type(message))
message = False
print (type(message))




