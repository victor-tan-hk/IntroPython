
firstNum = '35'
secondNum = '40'

sumNumber = firstNum + secondNum;
print("Adding two strings gives us ", sumNumber)

print("\nThe int() function converts from string to integer")
# This is an explicit conversion, i.e. specified by developer
# Also called type casting
sumNumber = int(firstNum) + int(secondNum);
print("Adding two numbers gives us ", sumNumber)


print("\nThis explicit conversion must be done when getting input from user, which is always in the form of a string")

num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")

print ("Concatenating the input as strings is ", ( num1 + num2))

print ("Converting input to numbers and then adding them is ",  int(num1)+int(num2) )


firstFloat = '2.56'
secondFloat = '3.22'
print("\nThe float() function converts from string to float")
sumNumber = float(firstFloat) + float(secondFloat)
print("Adding two floats gives us ", sumNumber)


firstVal = 2
secondVal = 3.5
print("\nImplicit conversion from lower data type (integer) to higher data type (float)")
print("This is done to avoid loss of data")
finalResult = firstVal + secondVal;

print ("The final result is ", finalResult);
print ("The final result is of type ", type(finalResult))


firstVal = 3;
secondVal = '35';
#The statement below will give an error as Python will not implicitly convert from string to int
#finalResult = firstVal + secondVal

print("\nThere is a need to explicitly convert from string to int")
finalResult = firstVal + int(secondVal)
print ("The final result is ", finalResult)


firstVal = 2
secondVal = 3.5
print("\nWe can also explicitly convert by downcasting from float to integer")
print ("This causes loss of accuracy due to the loss of decimal digits")
finalResult = firstVal + int(secondVal)
print ("The final result is ", finalResult)
