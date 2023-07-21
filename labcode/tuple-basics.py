
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#We can also create tuples without using parentheses
#However, this is not recommended as it can be confusing

my_tuple = 1, 2, 3
my_tuple = 1, "Hello", 3.4


#To define a tuple with one element, you need to include a 
#trailing comma after the first element. For example:
numbers = (3,)
print(type(numbers))   

# If you exclude the trailing comma, Python will interpret it
# as an int instead

numbers = (3)
print(type(numbers))    

#A tuple is basically an immutable list
#All the operations on a list that don't perform modification
#are available to a tuple


animals = ('cat','dog','rat','mouse','snake','monkey')

#Accessing via indexing
print(animals[0])   
print(animals[3])   
print(animals[-1])   
              

#Using slicing
print (animals[1:5])
print (animals[2:])
print (animals[:2])
print (animals[-2:])

#Iterating using a loop
for animal in animals:
    print(animal, end = ' ')
print("")

#Any attempt to modify an element in a tuple will result
#in an error
#animals[0] = "bird"

#Tuples also do not have the same methods as list
#that allow content modification, for e.g. append
#animals.append("elephant")
    
# Functions normally can return only one value
# Tuples are considered a single unit, so when
# you can return multiple values from a function
# by placing them in a tuple


def get_sum_and_avg(x, y, z):
    sum = x + y + z
    average = sum/3
    return(sum, average)

(S, A) = get_sum_and_avg(3, 8, 5)
print('Sum =', S)
print('Avg =', A)

#Tuples are also very useful as a shortcut
#when swapping values of two variables

x = 10
y = 20

print("Conventional approach to swapping")
temp = x
x = y
y = temp
print (f"After swapping, x is {x} and y is {y}")


print("Swapping using tuples")
x = 10
y = 20

(x, y) = (y, x)
print (f"After swapping, x is {x} and y is {y}")


