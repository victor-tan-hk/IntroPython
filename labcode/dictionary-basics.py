
#An empty dictionary
empty_dict = {}

#A dictionary with 5 key-value pairs
#Keys are typically strings 
#Values can be strings, int, bool and a list or 
#even another dictionary (nested dictionary)
person = {
    'first_name': 'Peter',
    'last_name': 'Parker',
    'age': 25,
    'favorite_colors': ['blue', 'green', 'red'],
    'married': True
}

print ("The number of key value pairs in this dictionary is ", len(person))
print (person)
print (type(person))
#Access values from dictionary using the key
print(person['first_name'])
print(person['age'])
print(person['favorite_colors'])
print(person['favorite_colors'][1])


#Attempting to access a key that doesn't exist
#causes a  KeyError

#print(person['salary'])

#To avoid this, use get, which returns a None
#if the key does not exist
# None, means that no value exists
salary = person.get('salary')
print (salary)

#Another way is to use the in operator
print ("salary" in person)
print ("age" in person)


#Dictionaries are mutable

#You can add new key-value pairs
person['gender'] = 'male'

#you can modify values of existing key-value pairs
person['age'] = 30

#you can delete existing key-value pairs
del person['married']
print ("After addition, modification, deletion:")
print (person)

print("Looping through all key-value pairs")
for k, v in person.items():
    print(f"{k}: {v}")
    
    
print("Looping through all the keys")    
for k in person.keys():
    print(k, end = ' ')
print ("")

print("Looping through all the values")    
for value in person.values():
    print(value, end = ' ')
print ("")

#You can use the unpacking ** operator 
#to merge two dictionaries
num_dict = {'a' : 1, 'b' : 2, 'c' : 3}
num_dict_2 = {'d' : 4, 'e' : 5, 'f': 6}
new_dict = {**num_dict, **num_dict_2}
print (new_dict)
    
#Dictionaries can contained other dictionaries as well
#This are called nested dictionaries    


people = {
    'person1' : {'name': 'John', 'age': 27, 'sex': 'Male'},
    'person2': {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    'person3': {'name': 'Jenny', 'age': 35, 'sex': 'Female'}
}

#Accessing values in a nested dictionary
print (people['person1']['name'])
print (people['person2']['age'])

#Adding new key-value pairs to a nested dictionary
people['person4'] = {'name': 'Peter', 'age': 42, 'sex': 'Male'}
print (people['person4'])

#Changing exsting values in a nested dictionary
people['person1']['name'] = 'Jason'

#Removing an existing key-value pair or element from
#a nested dictionary
del people['person2']
del people['person4']['age']

#Iterating through a nested dictionary
for p_id, p_info in people.items():
    print("\nPerson ID: ", p_id)
    
    for k, v in p_info.items():
        print(k + ':', v)

#List of dictionaries
persons = [
    {'name': 'John', 'age': 27, 'sex': 'Male'},
    {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    {'name': 'Jenny', 'age': 35, 'sex': 'Female'}
]

#Accessing elements in the list
print (persons[0])

#Accessing values in an element
print (persons[1]['sex'])

#Appending elements to the list
persons.append({'name': 'Peter', 'age': 42, 'sex': 'Male'})

print("Iterating through the list")
for person in persons:
    for k, v in person.items():
        print(k + ':', v)
        
#Rest of list operations the same




    