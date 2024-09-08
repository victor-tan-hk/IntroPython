
#Indentation is IMPORTANT in Python !!
# The statement below results in a compile time error
#    x = 5

print ("Demonstrating basic if")

#The 2 lines below the if are at the same indentation level
#Therefore they are treated as code block that is executed 
#as a single unit

age = int(input('Enter your age:'))

# All boolean expressions evaluate to either True or False
print (age >= 18)


if age >= 18:
    print("You're eligible to vote.")
    print("Let's go and vote.")

print("This statement is always executed regardless of the evaluation")

# Indentation ensures the 2 statements below the if and else 
# statement are treated as a single code block

print ("\nDemonstrating basic if-else")
# Change the value of number below to see which block gets executed

number = int(input("Enter a number : "))
if number > 0:
    print('Positive number')
    print ('This means its larger than zero')
else:
    print('Negative number')
    print('This means its smaller than zero')

print('This statement is always executed')


print ("\nDemonstrating if-elif-else with logical and operator")
# Change the value of bmi below to see which block gets executed
bmi = int(input("Enter a BMI : "))

weightStatus = ''

if bmi < 18.5: 
    weightStatus = 'Underweight'
elif (bmi >= 18.5 and bmi <= 24.9): 
    weightStatus = 'Normal'
elif  (bmi >= 25 and bmi <= 29.9): 
    weightStatus = 'Overweight'
elif (bmi >= 30 and bmi <= 34.9): 
    weightStatus = 'Obese'
elif (bmi >= 35 and bmi <= 39.9): 
    weightStatus = 'Severely obese'
elif (bmi > 40): 
    weightStatus = 'Morbidly obese'


print ("Your weight classification is ", weightStatus)


print ("\nYou can also have a final else in an if-else-if to cater for situations where none of the previous conditions are true")
# Change the value of weatherStatus below to see which block gets executed

weatherStatus = "something wierd"
if weatherStatus == 'rainy':
    print("I will order food online from Grab")
elif weatherStatus == 'sunny': 
    print("I will go out and have lunch with my friends")
elif weatherStatus == 'cloudy':
    print("I jog around the neighbourhood")
else: 
    print("I will just watch Netflix")

print ("\nDemonstrating ternary operator as a shortcut for standard if-else")

#Standard if-else
age = 20
message = ''
if age >= 18:
    message = "Yes, you can drive!"
else:
    message = "Sorry, you can’t drive yet!"
print(message)    

#Rewriting standard if-else with ternary operator
age = 20
message = ''
message = "Yes, you can drive!" if age >= 18 else "Sorry, you can’t drive yet!"
print(message)    

