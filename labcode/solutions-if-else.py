
# Q1

num = int(input("Enter a number : ")) 
if num % 5 == 0:
  print("Divisible by 5") 
else: 
  print("Not Divisible by 5")
  
  
#Q2 

amt = 0
nu = int(input("Enter number of electric units : "))
if nu <= 100:
    amt = 0
elif nu <= 200:
    amt = (nu-100) * 5
else:
    amt = 500 + ((nu - 200 ) * 10)
print(f"Amount to pay is : {amt}")

#Q3

marks = int(input("Enter your marks : "))
print ("You grade is : ", end = ' ')
if marks < 25:
  print ("F")
elif marks >= 25 and marks < 45:
  print ("E")
elif marks >= 45 and marks < 51:
  print ("D")
elif marks >= 51 and marks < 61:
  print ("C")
elif marks>= 61 and marks < 81:
  print ("B")
else:
  print ("A")

#Q4

first = int(input("Enter age of first person : "))
second = int(input("Enter age of second person : "))
third = int(input("Enter age of third person : "))

if first >= second and first >= third:
  print ("Oldest age is ",first)
elif second >= first and second >= third:
  print ("Oldest  age is ",second)
elif third >= first and third >= second:
  print ("Oldest age is ",third)
else:
  print ("All are equal age")	








