
#Basic approach of using a loop to populate an 
#empty list with values
print ("Using a loop to populate an empty list")
my_list = []
for num in range(5):
    my_list.append(num)
print (my_list)


#Shorter way of achieving the same effect
#with list comprehension
print ("Using list comprehension to populate an empty list")
new_list = [num for num in range(5)]
print(new_list)

print ("Slight variation on previous approach")
new_list = [num * 2 for num in range(5)]
print(new_list)

#Perform basic transformations on the values
#of an existing list to obtain a new list 
print ("Using list comprehension to transform an existing list")
animals = ['cat','dog','rat','mouse']
new_animals = [animal.upper() for animal in animals]
print(new_animals)


#You can use simple or complex conditional expressions with 
#list comprehension to filter out values from the 
#original iterable
print ("Only include even numbers between 0 and 20 in the list")
new_list = [num for num in range(20) if num % 2 == 0]
print(new_list)

print ("Only include even numbers between 30 and 50 in the list")
new_list = [num for num in range(50) if  num > 20 and num % 2 == 0]
print(new_list)

#Nested if with List comprehension
print("Only if y is divisible by both 5 and 2, it is added to new_list")
new_list  = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(new_list)


print("Create a new list of characters from a string")
new_list = [x for x in "superman"]
print(new_list)

print("Can also perform transformation on these characters")
new_list = [x.upper() for x in "superman"]
print(new_list)


#Nested list comprehensions work on sublists within list 
#i.e. multidimensional lists

print("Creating a multidimensional list using loops")

matrix = []
for i in range(3):
    # Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

print("Creating a multidimensional list using nested comprehension")

matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)


print("Performing transformations on items of multidimensional list using nested comprehension")

nested_list = [[1,2],[3,4],[5,6]]
new_list = [[x * 2 for x in sublist] for sublist in nested_list]
print(new_list)

print ("Flattening a multidimensional list with nested loop")
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
  
flatten_matrix = []
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
          
print(flatten_matrix)

print ("Flattening a multidimensional list with nested comprehension")
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
