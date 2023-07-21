
#using a traditional loop to double the value of the 
#list items

bonuses = [100, 200, 300]
new_bonuses = []
for bonus in bonuses:
    new_bonuses.append(bonus*2)
print(new_bonuses)


#using the map function to double the value of the 
#list items
def double(x):
    return x*2

#Obtain iterator first
iterator = map(double, bonuses)
#Convert iterator to a list
new_bonuses = list(iterator)
print(new_bonuses)

#To make this more concise, we use lambda function
#This avoids the need to define a separate function
iterator = map(lambda bonus: bonus*2, bonuses)
new_bonuses = list(iterator)
print(new_bonuses)

#Another example of map function to change all the items
#in a list of string to upper case

names = ['david', 'peter', 'jennifer']
new_names = list(map(lambda name: name.capitalize(), names))
print(new_names)

#You can use multiple iterators with map()
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = list(map(lambda n1, n2: n1+n2, num1, num2))
print(result)


# Sometimes you want to create a new list by filtering items 
# from an existing list

#Basic approach using loops
print ("Getting all the numbers from the first list that are larger than 70")
scores = [70, 60, 80, 90, 50]
filtered = []
for score in scores:
    if score >= 70:
        filtered.append(score)
print(filtered)

#Using the filter map to accomplish the same functionality
scores = [70, 60, 80, 90, 50]
filtered = list(filter(lambda score: score >= 70, scores))
print(filtered)

#Another example for filter
print("Getting all the strings that are shorter than 5 characters")
animals = ["cat","mouse","elephant","rat","alligator"]
filtered = list(filter(lambda x: len(x) < 5, animals))
print(filtered)


# Sometimes you want to perform an operation to reduce all the 
# items in a list to a single value
print ("Finding the sum of all the numbers in a list")
scores = [1, 2, 3, 4, 5]
total = 0
for score in scores:
    total += score
print("The sum of all numbers in the list is ", total)


print("Demonstrating how reduce works step-by-step")

from functools import reduce

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b

scores = [1, 2, 3, 4, 5]
total = reduce(sum, scores)
print("The sum of all numbers in the list is ", total)

#This can be made more concise with a lambda function
scores = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, scores)
print("The sum of all numbers in the list is ", total)

