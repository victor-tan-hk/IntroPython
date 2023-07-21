#Basic approach of using a loop to populate an 
#empty dictionary with values
print ("Using a loop to populate an empty dictionary")
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)


#Shorter way of achieving the same effect
#with dictionary comprehension
print ("Using dictionary comprehension to populate an empty dictionary")
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

#Perform basic transformations on the values
#of an existing dictionary to obtain a new dictionary
print ("Using dictionary comprehension to transform an existing dictionary")
us_price = {'milk': 2, 'coffee': 4, 'bread': 6, 'sugar': 10, 'tea': 12, "pasta": 14}

dollar_to_ringgit = 4
malaysia_price = {item: price * dollar_to_ringgit for (item, price) in us_price.items()}
print(malaysia_price)

#You can use simple or complex conditional expressions with 
#dictionary comprehension to filter out values from the 
#original iterable
expensive_items = {item: price for (item, price) in us_price.items() if price > 9}
print(expensive_items)

cheap_items = {item: price for (item, price) in us_price.items() if price < 11 if len(item) == 5}
print(cheap_items)

#You can use if-else in dictionary comprehension
#to transform either key or values in new dictionary
classify_items = {item: ('expensive' if price > 9 else 'cheap') for (item, price) in us_price.items() }
print(classify_items)

print("Nested dictionary comprehension to create nested dictionaries")

nest_dict = {
    k1: {k2: 'a' * k2 for k2 in range(1, 6)} for k1 in range(10, 51, 10)
}
print (nest_dict)


print("Nested dictionary comprehension to transform nested dictionaries")

#Change the string content of all the nested values
#to be uppercase
people = {
    'person1' : {'name': 'John', 'sex': 'Male'},
    'person2': {'name': 'Marie', 'sex': 'Female'},
    'person3': {'name': 'Jenny', 'sex': 'Female'}
}

new_people = { k1: {k2: v2.upper() for  (k2, v2) in v1.items() } for k1, v1 in people.items()}
print(new_people)

#Increase the age value of all the nested values
#by 30
young_people = {
    'person1' : {'name': 'John', 'age': 27, 'sex': 'Male'},
    'person2': {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    'person3': {'name': 'Jenny', 'age': 35, 'sex': 'Female'}
}

old_people = { k1: {k2: v2 + 30 if isinstance(v2,int) else v2 for (k2, v2) in v1.items() } for k1, v1 in young_people.items()}
print(old_people)



