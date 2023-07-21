
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


#You can provide escape characters preceded by \
validMessage = 'It\'s a nice day'
print (validMessage);

#Demonstrate the \n escape sequence character
print('First Line\nSecond Line\nThird Line')

#Demonstrate the \t escape sequence character
print('Word1\t\tWord2')


#A raw string treats the backslashes (\) as literal characters.
#Useful for working with directory locations

#This will give an error because the \U is interpreted as an escape sequence
#incorrectWindowsDir = "C:\Users\MyName\Desktop"

correctWindowsDir = "C:\\Users\\MyName\\Desktop"
print ("Windows path location ", correctWindowsDir)


#No such problem with Linux paths because / is NOT interpreted as escape sequence
myDirLocationLinux = "/usr/var/share"
print ("Linux path location ", myDirLocationLinux)

#We can use a raw string to simplify the writing of the Windows directory path

myDirLocationWindows = r"C:\Users\MyName\Desktop"
print ("Windows path location ", myDirLocationWindows)

#Creating a string that spans multiple lines using escape sequence characters

line_str = "I'm learning Python.\nIt is the best language for data science and automation.\nIt is very easy to learn."
print(line_str)

#Achieving the same effect using multi line string
#Keep in mind that escape character sequences still apply in multiline string
multiline_str = """
I'm learning\t\tPython.
It is the best language for data science and automation.
It is very easy to learn.
"""
print(multiline_str)


#You can combine raw strings and multiline strings together
#This will preserve all backslashes in the string and
#not interpret it as escape character sequences

raw_multiline_string = r"""This is a
raw multiline string
with backslashes \t and \n
that are not escaped."""
print (raw_multiline_string)


# 3 main ways of formatting string output

#1 Old Style String Formatting (% Operator)

name = 'Pete'
print('Hello %s' % name)

num = 5
print('I have %d apples' % num)

#
price = 22.6784
print('This cup costs %f dollars' % price)

#Rounding up to 2 decimal places
print('This cup costs %.2f dollars' % price)


#2 New Style String Formatting (str.format)

name = 'John'
age = 20

print("Hello I'm {}, my age is {}".format(name, age))


quantity = 3
itemno = 567
price = 49.321989
myorder = "I want {} pieces of item number {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price))



#3 String Interpolation / f-Strings (Python 3.6+)


name = 'Elizabeth'
print(f'Hello {name}!')


a = 5
b = 10
print(f'Five plus ten is {a + b}')
print(f'A more complex mathematical expression is { (2 * (a + b)) - 10 } ')      

#Multiline f-strings
message = (
f'Hi, {name}. \n'
f'You have {a} items on your shopping list'
)
print (message)

#Formatting long numbers with a comma separator
salary = 10000000
print (f"Your salary is {salary:,}")

#Rounding
pi = 3.1415926
print (f"Value of pi to 2 decimal places is {pi:.2f}")

#Percentage
passExam = 0.816562
print (f"Percentage of students who pass the exam is {passExam:.2%}")


print ("2 basic ways to concatenate two or more strings together")

#Using the + operator works for both literals and variables

s = 'Python ' + ' is' + ' fun'
print (s)
s1 = 'Java'
s2 = s1 + ' is' + ' exciting'
print(s2)


#Concatenating identical strings together multiple times using the * operator
s3 = s1 * 5
print (s3)

#Concatenating via the join method
s1, s2, s3 = 'Large', 'Black', 'Cat'
s4 = ' '.join([s1, s2, s3])
print(s4)

#Concatenating using the % formatting
s5 = '%s %s %s' % (s1, s2, s3)
print (s5)

#Concatenating using the format method
s6 = '{} {} {}'.format(s1, s2, s3)
print (s6)

#Concatenating using f-string
s7 = f'{s1} {s2} {s3}'
print (s7)

print("Using optional parameters of the print function to customize console output")

# Using end to replace the default newline escape character 
# without another character

print("mouse", end = ' ')
print("donkey", end = ' ')
print("horse")

print("chicken", end = ',')
print("zebra", end = ',')
print("snake")

#Using the sep to specify separating character between strings

#for formatting a date
print('09','12','2022', sep='-')
 
#formatting email
print('elonmusk','tesla.com', sep='@')



