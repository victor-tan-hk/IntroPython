


# Q1

sum = 0
n = int(input("Enter a  number : "))

for i in range(1, n + 1):
    # add current number to sum variable
    if i%2 ==0:
        sum += i
print("Sum is: ", sum)

# Q2

num = int(input("Enter a  number : "))
count = 0

while num != 0:
    num = num // 10
    count = count + 1

print(f"Total digits in original number is {count}")


# Alternative solution using a string

numStr = input("Enter a  number : ")
print (f"Total digits in original number is {len(numStr)}")

# Q3

start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))
print(f"Prime numbers between {start} and {end} are:")

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
            print(num)
            
            
#Q4


# first two numbers
num1, num2 = 0, 1

numTerms = int(input("Enter number of terms in Fibonacci sequence : "))
print("Fibonacci sequence:")

for i in range(numTerms):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res


#Q5

# First solution

digit = int(input("Select a digit x : "))
n = int(input("Select number of terms for digit x : "))

# first number of sequence
sum_seq = 0

start = digit
# run loop n times
for i in range(0, n):
    print(start, end=" + ")
    sum_seq += start
    # calculate the next term
    start = start * 10 + digit
print("\nSum of above series is:", sum_seq)

# Second solution


digit = input("Select a digit x : ")
n = int(input("Select number of terms for digit x : "))

# first number of sequence
sum_seq = 0
start = digit
# run loop n times
for i in range(0, n):
    print(start, end=" + ")
    sum_seq += int(start)
    # calculate the next term
    start += digit
print("\nSum of above series is:", sum_seq)


# Q6 


row = int(input("Enter the number of rows : "))

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(f'{j*i}', end = ' ')
    print("")


#Q7

rows = int(input("Enter the number of for the most asterisks : "))

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


