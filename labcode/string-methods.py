

#Capitalizes a string
txt = "python is awesome!"
print (txt.capitalize() + "\n")

#Converts string to uppercase
print(txt.upper() + "\n")

#Converts string to lowercase
txt = "PYTHON IS AWESOME"
print(txt.lower() + "\n")

# checks if all the letters are uppercase.
print(txt.isupper())

# checks if all the letters are lowercase.
print(txt.islower())

# checks if all the characters are numeric.
print(txt.isnumeric())

# checks if all the characters are in the alphabet.
# this returns false since the string contains spaces
print(txt.isalpha())

txt = "PYTHON"
print(txt.isalpha())

print()

# returns the number of occurrences of a substring in the given string.

string = "Python is awesome, isn't it?"
substring = "is"
print ("The substring occurs in the main string this many times: ", string.count(substring))


# String characters are indexed from 0
# returns the index of first occurrence of the substring (if found). # If not found, it returns -1.
message = 'Python is a fun programming language'

# check the index of 'fun'
print("fun occurs at position ", message.find('fun'))
print("boring occurs at position ", message.find('boring'))


# replaces each matching occurrence of a substring with another string.
text = 'bat ball'

replaced_text = text.replace('ba', 'ro')
print("After replacement, we have", replaced_text)

