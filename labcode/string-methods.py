

print("\nCapitalizes a string")
txt = "python is awesome!"
print (txt.capitalize())

print("\nConverts string to uppercase")
print(txt.upper())

print("\nConverts string to lowercase")
txt = "PYTHON IS AWESOME"
print(txt.lower())

print("\nChecks if all the letters are uppercase.")
print(txt.isupper())

print("\nChecks if all the letters are lowercase.")
print(txt.islower())

print("\nChecks if all the characters are numeric.")
# This returns false since all the characters are alphabets
print(txt.isnumeric())

# This returns true since all the characters are numbers
numericStr = "12345"
print(numericStr.isnumeric())

print("\nChecks if all the string characters are in the alphabet.")
txt = "PYTHON"
print(txt.isalpha())

# this returns false since the string contains spaces
strwithspaces = "PYTHON IS COOL"
print(strwithspaces.isalpha())


print("\ncount method returns the number of occurrences of a substring in the given string.")

string = "Python is awesome, isn't it?"
substring = "is"
print ("The substring occurs in the main string this many times: ", string.count(substring))


print ("\nreplace method replaces each matching occurrence of a substring with another string.")
text = 'bat ball'

replaced_text = text.replace('ba', 'ro')
print("After replacement, we have", replaced_text)