
# This is a comment, it will be ignored by the interpreter

# The sequence of characters is a string, can be delimited by either 
# single quotes or double quotes
print("Hello there !")
print('This is my first python program')

# Notice that there is NO semicolon at the end of the statements above


#Declaring two variables a and b
#Assigning the values 10 and 20 to them
a = 10
b = 20 #Inline comments appear at the end and on the same line as a statement

''' This is an example of a multiline comment 
using triple quotes that are meant 
for multi-line strings

Declaring variable c
Assigning the sum of a and b into it '''

c = a + b

# Displaying the content of variables via the print function
print ("The value of a is ", a)
print ("The value of b is ", b)
print ("The value of c is ", c)

# We can reassign new values into a variable after the initial assigment
a = 100
b = 200

#Python supports assigning multiples values to multiple variables in a single line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Python supports assigning the same value to multiple variables in a single line

x = y = z = "Superman"
print(x)
print(y)
print(z)

# Constants are not explicitly supported in Python
# They are enforced implictly through naming convention

#This means that PI should be a constant and NEVER be changed
PI = 3.14

#However, even if you try to change it, the compiler will not complain
PI = 111.11



#Using multi line statements
#Extending the statement over multiple lines using the continuation character \
    
addition = 10 + 20 + \
           30 + 40 + \
           50 + 60 + 70
print("Adding 10 to 70 gives us", addition)

# Getting input from user via the input function
name = input("Please tell me your name : ")
print ("Hello there ",name)




