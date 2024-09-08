
#Accessing string characters using index notation
str = "Python String"
print(str[0]) # P
print(str[1]) # y

#use a negative index to return the characters starting from the end of the string. 

print(str[-1])  # g
print(str[-2])  # n


print("The length of str is", len(str))

print("Examples of slicing a string")
print(str[0:6])
print(str[7:])


#Python strings are immutable, unlike lists
#Trying to change any character in it results in an error.

#This gives an error
#str[0] = 'J'


#To modify a string, you need to create a new one from the existing string
new_str = 'J' + str[1:]
print(new_str)


# iterating through characters in a string using a for loop
for letter in str:
    print(letter)

# Although a string is a sequence of characters
# and can have list operations applied on it
# it is considered to be different from a list containing characters
firstWord = ['c','a','t']
print (type(firstWord))
secondWord = "cat"
print (type(secondWord))

#You can create a list of characters from  a string
#using the list function
text = "Superman"
text_list = list(text)
print (text_list)


print("\nMany string methods return the index of a specific character in the list of characters")


print("find method returns the index of first occurrence of the substring if it is found. If it is not found, it returns -1.")

message = 'Python is a fun programming language'

# check the index of 'fun'
print("fun occurs at position ", message.find('fun'))
print("boring occurs at position ", message.find('boring'))







#Demonstrating that a string is immutable
#the id function gives the memory address of the object 
#that a variable references
a = "cat"
print ("Memory address of object that a references is : ", id(a))

#All string methods create a new object
#The original object is left unchanged
print(a.upper())
print(a)
print ("Memory address of object that a references is : ", id(a))

#Assigning the new object to b
#Both b and a are point to different objects
b = a.upper()
print ("Memory address of object that a references is : ", id(a))
print ("Memory address of object that b references is : ", id(b))


