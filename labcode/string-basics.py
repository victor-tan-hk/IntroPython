
#Strings can be delimited with either single quotes ' '  or double quotes " "
message = 'This is a string in Python'
message = "This is also a string"

#With double quotes, you can have single quotes within the string
validMessage = "It's a nice day"

#With single quotes, you can have double quotes within the string
validMessage = 'Is this quote "A cat has nine lives" true ?? '

#If you try to nest single quotes within single quotes,you get a compiler error
#invalidMessage = 'It's a nice day'

#Same comments apply to nest double quotes within double quotes
#invalidMessage = "Is this quote "A cat has nine lives" true ?? "


print("You can provide escape characters preceded by the back slash")
validMessage = 'It\'s a nice day'
print (validMessage);

#Demonstrate the \n escape sequence character
print('First Line\nSecond Line\nThird Line')

#Demonstrate the \t escape sequence character
print('Word1\t\tWord2')




#This will give an error because the \U is interpreted as an escape sequence
#incorrectWindowsDir = "C:\Users\MyName\Desktop"

#To use a \ directly in a string, we need to make it an escape sequence
#character with \\
print ("Using backslash in a string to designate a Windows directory locations")

correctWindowsDir = "C:\\Users\\MyName\\Desktop"
print ("Windows path location ", correctWindowsDir)


#No such problem with Linux paths because forward slash / is NOT interpreted as escape sequence
myDirLocationLinux = "/usr/var/share"
print ("Linux path location ", myDirLocationLinux)


#A raw string treats the backslashes (\) as literal characters.
#Useful for specifying Windows-based directory locations

print("\nUse a raw string to simplify the writing of the Windows directory path")

myDirLocationWindows = r"C:\Users\MyName\Desktop"
print ("Windows path location ", myDirLocationWindows)

print("\nCreating a string that spans multiple lines using escape sequence characters")

line_str = "\nI'm learning Python.\nIt is the best language for data science and automation.\nIt is very easy to learn."
print(line_str)

print("\nAchieving the same effect using multi line string that is delimited at start and end with 3 double quotes")
print("Escape character sequences still apply in multiline string")
multiline_str = """
I'm learning\t\tPython.
It is the best language for data science and automation.
It is very easy to learn.
"""
print(multiline_str)


print("\nYou can combine raw strings and multiline strings together")
#This will preserve all backslashes in the string and
#not interpret it as escape character sequences

raw_multiline_string = r"""
This is a
raw multiline string
with backslashes \t and \n
that are not escaped."""
print (raw_multiline_string)


print("\nFormatting string output using string Interpolation / f-Strings (Python 3.6+)")

name = 'Elizabeth'
print(f'Hello {name}!')

a = 5
b = 10
print(f'Five plus ten is {a + b}')
print(f'A more complex mathematical expression is { (2 * (a + b)) - 10 } ')      

print ("\nMultiline f-strings are delimited with () ")
message = (
f'Hi, {name}. \n'
f'You have {a} items on your shopping list'
)
print (message)

print("\nFormatting long numbers in multiline string with a comma separator")
salary = 10000000
print (f"Your salary is {salary:,}")

print("\nRounding decimal numbers in multiline string to specific number of places")
#Rounding
pi = 3.1415926
print (f"Value of pi to 2 decimal places is {pi:.2f}")

#Percentage
print("\nDisplaying a decimal number in the form of a percentage in multiline string")
passExam = 0.816562
print (f"Percentage of students who pass the exam is {passExam:.2%}")


print ("\nConcatenating strings is a very common operation")
print ("Some common approaches to performing it")

print("\nApproach 1: Using the + operator works for both literals and variables")

s = 'Python ' + ' is' + ' fun'
print (s)
s1 = 'Java'
s2 = s1 + ' is' + ' exciting'
print(s2)


print("\nApproach 2: Concatenating identical strings together multiple times using the * operator")
s3 = s1 * 5
print (s3)

print("\nApproach 3: Concatenating via the join method, where you can also specify a separator between the concatenated strings")

s1, s2, s3 = 'Large', 'Black', 'Cat'
s4 = ' '.join([s1, s2, s3]) # Separator space 
print(s4)
s5 = ','.join([s1, s2, s3]) # Separator ,
print(s5)
s6 = ':'.join([s1, s2, s3]) # Separate :
print(s6)



print ("\nApproach 4: Concatenating using f-string")
s7 = f'{s1} {s2} {s3}'
print (s7)

