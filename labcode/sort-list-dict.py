

numbers = [11, 3, 7, 5, 2]

#Default sort order is ascending
print ("Sort in ascending order")
numbers.sort()
print (numbers)


print ("Sort in descending order")
numbers = [11, 3, 7, 5, 2]
numbers.sort(reverse=True)
print (numbers)

#There is also an optional sorted function
#The difference between sort() and sorted() is: 
#sort() changes the list directly 
# sorted() doesn't change the list 
#instead it returns a new sorted list.

print("Demonstrating the sorted function")
numbers = [11, 3, 7, 5, 2]

#Default sort order is alphabetical
new_numbers = sorted(numbers)

print (numbers)
print(new_numbers)

print("Strings are sorted in order according to ASCII code")
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()
print(guests)

letters = ['R','p','Q','b','C']
letters.sort()
print(letters)

#you can provide your own custom implementation 
#for sorting using the key parameter
#which you pass a function that will
#operate on all the elements of the list
#and return an actual value that is used in sorting

print ("Demonstrate custom sort implementation")
somestrings = ['cccc', 'aaa', 'bbbbbb', 'zz', 'eeeeee', ]
somestrings.sort()
print(somestrings)

somestrings = ['cccc', 'aaa', 'bbbbbb', 'zz', 'eeeeee', ]
somestrings.sort(key=len)
print(somestrings)

#To sort a list of dictionaries based on specific
# values in the dictionaries, we will need to use 
# custom sort
persons = [
    {'name': 'John', 'age': 27, 'sex': 'Male'},
    {'name': 'Marie', 'age': 23, 'sex': 'Female'},
    {'name': 'Jenny', 'age': 35, 'sex': 'Female'},
    {'name': 'Peter', 'age': 20, 'sex': 'Female'}

]

def getAge(item):
    return item['age']

def getName(item):
    return item['name']

print ("Sorting list of dictionaries on age")
sortOnAge = sorted(persons, key=getAge)
print (sortOnAge)

print ("Sorting list of dictionaries on name")
sortOnName = sorted(persons, key=getName)
print (sortOnName)

print("Using lambda functions to simplify code")
sortOnAge = sorted(persons, key = lambda item: item['age'])
print (sortOnAge)

sortOnName = sorted(persons, key = lambda item: item['name'])
print (sortOnName)


#For sorting dictionaries we have to use the custom
#implementation sort and specify a function for the 
#key parameter

print ("Demonstrating sorting dictionaries")
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

#The items method breaks the pairs into keys (location 0) 
# and values (location 1), and the lambda function
# retrieves the values --> x[1]

sorted_footballers_by_goals = sorted(footballers_goals.items(), key = lambda x : x[1])
print(sorted_footballers_by_goals)

#Notice that the result is a list of tuples
#We may wish to convert it back again to a normal dictionary
finalSortedResult = dict(sorted_footballers_by_goals)
print (finalSortedResult)


