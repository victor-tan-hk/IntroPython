

# Conventional way of extracting values from 
# list using index notation and assigning them
# to separate variables

colors = ['red', 'blue', 'green']
x = colors[0]
y = colors[1]
z = colors[2]

#Short cut of the above using unpacking

a, b, c = colors
print (f"a is {a}, b is {b}, c is {c}")

# For this to work you must have the exact
# number of variables on the left hand side
# as the number of items in the list
# Below will result in an error

#p, q = colors

# If you want to unpack the first few elements of a list 
# and don’t care about the other elements, you can:
# First, unpack the needed elements to variables.
# Second, pack the leftover elements into a new list 
# and assign it to another variable.

animals = ('cat','dog','rat','mouse','snake','monkey')
#The * operator packs the remaining items in the list
#into a new sublist other
a, b, *other = animals
print (f"a is {a}, b is {b}, other is {other}")

#You can unpack two tuples and marge them into a single tuple 
#using the *operator on the right hand side

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
numbers = (*odd_numbers, *even_numbers)
print(numbers)





