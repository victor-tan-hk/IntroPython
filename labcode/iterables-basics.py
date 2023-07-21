
# define a list
my_list = [4, 7, 6]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  

# get the second element of the iterator
print(next(iterator))  

# get the third element of the iterator
print(next(iterator))  

#The iterator has now reached the end
#Calling next on it will result in an error

#print(next(iterator))  


def use_iterator(iterator):
    print ((type(iterator)))
    for element in iterator:
        print(element)
        
#Common iterables
#List, Tuple, Dictionary, String 
#Also set (not shown)
my_list = [4, 7, 6, 9, 10]
my_tuple = (1, 2, 3, 4, 5)
my_string = "abcdefg"
my_dict = {
    'first_name': 'Peter',
    'last_name': 'Parker',
    'age': 25,
    'favorite_colors': ['blue', 'green', 'red'],
    'married': True
}

use_iterator(iter(my_list))
use_iterator(iter(my_tuple))
use_iterator(iter(my_string))
use_iterator(iter(my_dict))



