# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 08:54:08 2024

@author: User
"""



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

# Related to concept that everything in Python is an object !

print ("Python is a dynamically typed language")
print ("You can assign values of different types to the same variable")
message = 'Hello';
print (type(message))
message = 100
print (type(message))
message = 3.96
print (type(message))
message = False
print (type(message))


# Different ways of formatting string output
print ("\nApproach #1:Old Style String Formatting (% Operator) ")

name = 'Pete'
print('Hello %s' % name)

num = 5
print('I have %d apples' % num)


price = 22.6784
print('This cup costs %f dollars' % price)

#Rounding up to 2 decimal places
print('This cup costs %.2f dollars' % price)


print ("\nApproach #2:New Style String Formatting (str.format) ")

name = 'John'
age = 20

print("Hello I'm {}, my age is {}".format(name, age))


quantity = 3
itemno = 567
price = 49.321989
myorder = "I want {} pieces of item number {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price))


#Concatenating strings using older formatting approach


print ("\nApproach 4: Concatenating using the % formatting")
s7 = '%s %s %s' % (s1, s2, s3)
print (s7)

print ("\nApproach 5: Concatenating using the format method")
s8 = '{} {} {}'.format(s1, s2, s3)
print (s8)



print("\nUsing optional parameters of the print function to customize console output")

print ("Using end parameter to replace the default newline escape character with space");
print("mouse", end = ' ')
print("donkey", end = ' ')
print("horse")

print ("\nUsing end parameter to replace the default newline escape character with comma");
print("chicken", end = ',')
print("zebra", end = ',')
print("snake")

print("\nUsing the sep parameter to specify separating character between strings")

print ("Using - for formatting dates")
print('09','12','2022', sep='-')
 
print ("Using @ for formatting email")
print('elonmusk','tesla.com', sep='@')

