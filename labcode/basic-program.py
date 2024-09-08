

print("Hello there !")

print('This is my first python program')

# This is a single comment, it will be ignored by the interpreter

# Notice that there is NO semicolon at the end of the statements above

# The sequence of characters delimited by either 
# single quotes or double quotes is called in a string



#Declaring two variables a and b

#Assigning the numeric values 10 and 20 to them
a = 10

b = 20 #Inline comments appear at the end and on the same line as a statement



''' This is an example of a multiline comment 
using triple quotes that are meant 
for multi-line strings

Declaring variable c
Assigning the sum of a and b into it '''

c = a + b

# Displaying the content of variables via the print function

print ("")
print ("The value of a is ", a)
print ("The value of b is ", b)
print ("The value of c is ", c)

# We can reassign new values into a variable after the initial assigment

a = 100
b = 200

# Repeat the addition operation and store in variable c
c = a + b

# Displaying the new content in the variables via the print function

print ("")
print ("The new value of a is ", a)
print ("The new value of b is ", b)
print ("The new value of c is ", c)



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

#We can use the standard arithmetic operators to create mathematical expressions
#which can be evaluated, and the result stored in a variable or printed out

#https://www.idtech.com/blog/important-math-formulas-for-school-students

pi = 3.1416
radius = 4

circumference_circle = 2 * pi * radius
area_circle = pi * (radius ** 2)

print ("")
print ("Circumference of circle with radius of 4 is : ",circumference_circle)
print ("Area of circle with radius of 4 is : ",area_circle)


#Computing distance between 2 points on a 2D plane

#Coordinates for point 1
x1 = 5
y1 = 10


#Coordinates for point 2
x2 = 3
y2 = 20


# We need to use parenthesis in order to ensure that the expression is
# evaluated in the correct order
distance1 = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print ("")
print ("The distance between the two points x1,y1 and x2,y2 is", distance1)


# We can use the sqrt and pow function from the math library in Python to 
# obtain the same result

#First we need to import the library
import math

#Then we use the sqrt and pow functions in the library

distance2 = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))

print ("The distance between the two points x1,y1 and x2,y2 is", distance1)

