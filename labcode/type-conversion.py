
firstNum = '35'
secondNum = '40'

sumNumber = firstNum + secondNum;
print("Adding two strings gives us ", sumNumber)

# The int() function converts from string to integer
# This is an explicit conversion, i.e. specified by developer
# Also called type casting
sumNumber = int(firstNum) + int(secondNum);
print("Adding two numbers gives us ", sumNumber)


#This explicit conversion must be done when getting input from user, which is always in the form of a string

num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")

print ("Concatenating the input as strings is ", ( num1 + num2))

print ("Converting input to numbers and then adding them is ",  int(num1)+int(num2) )

firstFloat = '2.56'
secondFloat = '3.22'
# The float() function converts from string to float
sumNumber = float(firstFloat) + float(secondFloat)
print("Adding two floats gives us ", sumNumber)


firstVal = 2
secondVal = 3.5
#Implicit conversion from lower data type (integer) to higher data type (float)
#This is done to avoid loss of data
finalResult = firstVal + secondVal;

print ("The final result is ", finalResult);
print ("The final result is of type ", type(finalResult))


firstVal = 3;
secondVal = '35';
#The statement below will give an error as Python will not implicitly convert from
#string to int
#finalResult = firstVal + secondVal

#We will need to explicitly convert it ourselves
finalResult = firstVal + int(secondVal)
print ("The final result is ", finalResult)


firstVal = 2
secondVal = 3.5
# We can explicit convert by downcasting
# this causes loss of data
finalResult = firstVal + int(secondVal)
print ("The final result is ", finalResult)
