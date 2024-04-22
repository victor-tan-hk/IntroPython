
#Using range function to control the number of iterations 
#of the for loop
#Notice that the body of the loop must be indented
#as a separate code block

#Range generates a sequence of numbers
#starting from 0 to n-1 (where n is the argument passed to it)
#increment by 1
print("Basic use of range")
for index in range(5):
    print(index)
    
print("\nUse of range with start / stop values specified")
# You can specify the start and stop values for the range function
#It will generate numbers between start and stop-1
#Be EXTREMELY CAREFUL with this to avoid a miss by 1 loop error

for index in range(3, 8):
    print(index)   
    
print("\nUse of range with increment specified")
# In addition to start and stop, you can also include the 
# increment as the 3rd argument to the range function

for index in range(5, 30, 5):
    print(index)  
#Notice that the numbers generated does not include
#30, since the generation is only up to stop-1 (29) 

print("\nIncrement can be used for a loop that counts backwards")
for index in range(20, 9, -2):
    print(index)  



print("\nA common use of the loop is to accumulate the sum of multiple values.")
# For e.g. to find the sum of 1, 2, 3, 4, 5

sum = 0
for i in range (1, 6):
    sum += i
print("The sum of 1 to 5 is ", sum)


# Another simple use case: 
print("\nCalculate savings  with compounded interest over a certain number of years")

savings = 2000
numyears = 5
interestRate = 10 # this means 10%

for year in range (1, numyears+1):
    savings += savings * interestRate / 100
    print(f'Accumated savings at the end of year { year} is {savings}')      

    



print("\nFirst approach to printing all odd numbers between 1 and 10")

for i in range (1, 11, 2):
    print (i)
    
#We can include if-else statements within the loop body
#to implement specific logic    
print("\nSecond approach to printing all odd numbers between 1 and 10 using if-else logic")

for i in range (1, 11):
    if i % 2 == 1:
        print (i)


# Loops can be nested

print("\nA simple use case for nested loops: Multiplication tables")

for x in range (10, 14):
    print(f"**** Multiplication table for {x} ****")
    for y in range (1, 11):
        print(f"{x}  x  {y} = {x * y}")


print ("\nThe range function is implemented ")
print ("to prevent infinite loop due to incorrect increments")
# A potential infinite loop situation below
# No values returned from the range function
# This prevents an accidental infinite loop from locking up the program
for x in range (1, 10, -1):
    print (x)




   