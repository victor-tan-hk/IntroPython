
#Can declare an empty list
empty_list = []

#Lists with predefined content: strings and numbers
animals = ['cat','dog','rat','mouse']
numbers = [5, 8, 2, 15, 9, 4]

print (animals)
print (numbers)
print (type(numbers))

# list can store elements of different data types
# however this is not common use, as it can complicate
# processing the list
list1 = [1, "Hello", 3.4, False]

# list can store duplicate elements
list2 = [1, "Hello", True, 3.4, "Hello", 1, True]

#Accessing element in lists via normal indexing
print ("First element in animals is ", animals[0])
print ("Fourth element in animals is ", animals[3])

#Accessing elements via negative indexing
print ("Last element in numbers is ", numbers[-1])
print ("Second last element in numbers is ", numbers[-2])

print ("Modifying elements in a list")
numbers[0] = 10
numbers[1] = 20
print (numbers)

print ("Finding the size (number of elements) of a list")
print (f"numbers list has {len(numbers)} items in it")
print (f"animals list has {len(animals)} items in it")

print ("Adding elements to the end of a list")
animals.append("snake")
animals.append("cow")
print (animals)


print("Adding a list to the end of another list")
extra_numbers = [200,300,400]
numbers.extend(extra_numbers)
print (numbers)

print("Using the * unpacking operator to merge two lists")
num_list_1 = [1,2,3,4,5]
num_list_2 = [6,7,8,9,10]
new_num_list = [*num_list_1, *num_list_2]
print (new_num_list)

print ("Inserting elements in the middle of a list")
animals.insert(2, "donkey")
print (animals)

print ("Deleting elements from a list based on index position")
del animals[1]
print (animals)

print ("Removing the last element from the list and returning it")
lastEl = animals.pop()
print (animals)
print ("The last element which was removed :",lastEl)

print ("Deleting elements from a list based on element value")
animals.remove("mouse")
print (animals)

print("Locating the index position of a particular element in the list")
ratLocation = animals.index('rat')
print ("Rat is located at index ", ratLocation)

#attempting to use index when the element does not exist 
#results in a  ValueError
#uncomment below to see error
#unknown = animals.index("elephant")

#To avoid this, use in operator to check for membership in a list
#Change the value of animalToLookFor to verify
animalToLookFor = 'snake'
if animalToLookFor in animals:
    animalIndex = animals.index(animalToLookFor)
    print(f"The {animalToLookFor} has an index of {animalIndex}.")
else:
    print(f"{animalToLookFor} doesn't exist in the list.")

#Using for to iterate through a list
for animal in animals:
    print(animal)
    
print ("Finding the sum of all elements larger than 100 in the numbers list")

sum = 0
for num in numbers:
    if num > 100:
        sum += num
print ("The sum of all elements larger than 100 in the numbers list is : ", sum)

# Using the for loop does not allow you to access the 
# index position of the element. To achieve this, you 
# need to use the enumerate function
print("Index position and element in the animals list")
for index, animal in enumerate(animals):
    print(f"{index}: {animal}")

#Lists can also contain other lists (multi-dimensional lists)
print ("Multidimensional lists")

table = [
    [10, 11, 12, 13, 14, 15],
    [20, 21, 22, 23, 24, 25],
    [30, 31, 32, 33, 34, 35],
    [40, 41, 42, 43, 44, 45],
]

print ("Item at first row third column : ",table[0][2])
print ("Item at third row sixth column : ",table[2][5])

#Using a nested loop to print out the contents 
#of the multidimensional table
for i in range(len(table)) : 
    for j in range(len(table[i])) : 
        print(table[i][j], end=" ")
    print()


