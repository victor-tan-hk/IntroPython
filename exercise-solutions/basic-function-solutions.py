
# Q1


def calculateSumEven(n):
    sum = 0
    for i in range(1, n + 1):
        # add current number to sum variable
        if i%2 ==0:
            sum += i
    return sum
        
    
n = int(input("Enter a  number : "))

print("Sum is: ", calculateSumEven(n))


# Q3

def getPrimes(start, end):
    stringPrimes = ""
    for num in range(start, end + 1):
        # all prime numbers are greater than 1
        # if number is less than or equal to 1, it is not prime
        if num > 1:
            for i in range(2, num):
                # check for factors
                if (num % i) == 0:
                    # not a prime number so break inner loop and
                    # look for next number
                    break
            else:
                stringPrimes = stringPrimes + str(num) + " , "
    return stringPrimes
    

start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))
result = getPrimes(start,end)
print(f"Prime numbers between {start} and {end} are {result}")



#Q5

def sumOfTerms(x, n):
    # first number of sequence
    sum_seq = 0
    
    start = digit
    # run loop n times
    for i in range(0, n):
        print(start, end=" + ")
        sum_seq += start
        # calculate the next term
        start = start * 10 + digit
    return sum_seq
   
digit = int(input("Select a digit x : "))
n = int(input("Select number of terms for digit x : "))

print("\nSum of above series is:", sumOfTerms(digit,n))
