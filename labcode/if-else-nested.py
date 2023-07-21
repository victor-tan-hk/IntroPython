
# Nested if-else logic to implement this use case

# If client earns more than 5000 a month and is married 
# and have EPF savings of at least 60000, then client
# qualifies for the loan 

print("Loan Example #1")
# Change the values here to test out the logic of the conditional statement
monthlySalary = 8000
isMarried = True
epfSavings = 70000

# Demonstrating nested-if
# make sure you match the indentation levels correctly
if monthlySalary > 5000: 
    print("Monthly salary more than 5000. One step closer !")
    if isMarried: 
        print("You are married. Another step closer !")
        if epfSavings >= 60000: 
            print("You qualify for the loan. Yay !")
        else: 
            print ("Sorry ! You don't qualify ....")

    else: 
        print ("Sorry ! You don't qualify ....")
else: 
    print ("Sorry ! You don't qualify ....")



# If the intermediate output statements are not required,
# this can be written more simply as:

print("Loan Example #1 - Repeated in simpler form")

if (monthlySalary > 5000 and isMarried and epfSavings >= 60000): 
    print("You qualify for the loan. Yay !")
else:
    print ("Sorry ! You don't qualify ....")


# Nested if-else logic to implement the 2nd use case

# Conditions to qualify for the loan
# 1. if you earn 5000 or more a month and you have EPF savings of at least 60000
# 2. if you earn less than 5000 a month and you have EPF savings of at least 80000
# 3. if you are married and both you and your spouse together earn 10000 or more a month and your EPF savings is at least 30000 


print("Loan Example #2")
# Change the values here to test out the logic of the conditional statement
spouseMonthlySalary = 8000
monthlySalary = 2000
isMarried = True
epfSavings = 70000

if isMarried: 
    
    if spouseMonthlySalary + monthlySalary >= 10000:
        if epfSavings >= 30000: 
            print("You qualify for the loan. Yay !")
        else: 
            print ("Sorry ! You don't qualify ....")
    else: 
        print ("Sorry ! You don't qualify ....")
     
else: 

    if (monthlySalary >= 5000 and epfSavings >= 60000):
        print("You qualify for the loan. Yay !")
    elif (monthlySalary < 5000 and epfSavings >= 80000):
        print("You qualify for the loan. Yay !")
    else:    
        print("Sorry ! You don't qualify ....")


# Rewriting the same logic above in simpler form

print("Loan Example #2 - Repeated in simpler form")

qualifyForLoan = False

if (isMarried and (spouseMonthlySalary + monthlySalary >= 10000) and epfSavings >= 30000):
    qualifyForLoan = True
elif (monthlySalary >= 5000 and epfSavings >= 60000):
    qualifyForLoan = True
elif (monthlySalary < 5000 and epfSavings >= 80000):
    qualifyForLoan = True

if qualifyForLoan:
    print("You qualify for the loan. Yay !")
else:    
    print("Sorry ! You don't qualify ....")


