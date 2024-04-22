
#While loop requires a loop counter
#which is incremented within the loop body
#and a check using this loop counter in the 
#while statement test condition

print ("Basic while loop with a counter")
max = 5
counter = 0
while counter < max:
    print(counter)
    counter += 1




# A classic use case for while loop is to
# obtain input from user repeatedly until
# a specific termination value is entered

# Program to obtain numbers from user
# and calculate their total sum 

print ("\nLoop to obtain numbers from user")
print ("Sums these numbers together")
print ("Continue until the user enters 0")

total = 0
number = int(input('Enter a number (0 to exit): '))
# add numbers until number is zero
while number != 0:
    total += number    
    number = int(input('Enter a number (0 to exit): '))
    
print('Total of all numbers entered =', total)

print ("\nWhile loops can result in infinite loops if you are not careful")

#If you uncomment the loop below, the while condition will never be false
#The loop never stops, you will have to press Ctrl-C in IPython console to exit

# stop = 0
# counter = 1
# while counter > stop:
#     print(counter)
#     counter += 1

