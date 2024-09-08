

#Terminate a for loop prematurely when a specific condition is true using break
print ("Demonstrating break in a for loop")
for index in range(0, 10):
    print(index)
    if index == 3:
        break
    

print("\nWhen used inside a nested loop, break will terminate only the innermost loop")

for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y > 2:
            break
        print(f"(x : {x}, y : {y})")


print("\nTypical use case for break: Terminate a while loop that is infinite based on user input")

while True:
    userEntry = input('Enter an input (type Q to quit): ')
    if userEntry.lower() == 'q':
        break
    print ("You entered : ", userEntry)
    
# continue statement skips the remaining statements in 
# the code block and continues with the next iteration 

print ("\nDemonstrating continue in a for loop")
for index in range(0, 5):
    #This causes the printing of 2 to be skipped
    if index == 2:
        continue
    print(index)

# using continue in a while loop
# We print out only odd numbers by skipping the print
# when the numbers are even
print ("\nDemonstrating continue in a while loop")
counter = 0
while counter < 10:
    counter += 1

    if counter % 2 == 0:
        continue

    print(counter) 


# pass is used as a place holder for a statement
# that should be there in order to avoid a compiler error

#Using pass with an if else
x = 10
if x < 5:
    print ("x is small")
else:
    pass

#If you comment out the pass keyword above, 
# the compiler will flag an error in the next line of code below

#Using pass with a loop

for i in range (5):
    pass




