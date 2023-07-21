
#Indentation is IMPORTANT in Python !!
# The statement below results in a compile time error
#    x = 5

print ("Demonstrating basic if")

#The 2 lines below the if are at the same indentation level
#Therefore they are treated as code block that is executed 
#as a single unit

age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")
    print("Let's go and vote.")

print("This statement is always executed regardless of the evaluation")

# Indentation ensures the 2 statements below the if and else 
# statement are treated as a single code block

print ("Demonstrating basic if-else")
number = 10
if number > 0:
    print('Positive number')
    print ('This means its larger than zero')
else:
    print('Negative number')
    print('This means its smaller than zero')

print('This statement is always executed')


print ("Demonstrating if-elif-else with logical and operator")
bmi = 21
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

# You can also have a final else in an if-else-if to cater
# for situations where none of the previous conditions are true
weatherStatus = "something wierd"
if weatherStatus == 'rainy':
    print("I will order food online from Grab")
elif weatherStatus == 'sunny': 
    print("I will go out and have lunch with my friends")
elif weatherStatus == 'cloudy':
    print("I jog around the neighbourhood")
else: 
    print("I will just watch Netflix")

print ("Demonstrating ternary operator")

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

#Ternary operator can also be used to simplify if-elif-else
#However not recommended as the code is hard to understand

#Standard if-elif-else
x = -1
if x < 0:
    print('x is less than zero')
elif x > 0:
    print('x is greater than zero')
else:
    print('x is equal to 0')


#Implementation with ternary operator
x = -1
message = ''
message = 'x is less than zero' if x < 0 else 'x is greater than zero' if x > 0 else 'x is equal to 0'
print (message)
