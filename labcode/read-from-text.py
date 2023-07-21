

#Reads the text file as a single string
with open('the-zen-of-python.txt') as f:
    contents = f.read()
    print(type(contents))
    print (contents)


#Reads the text file as a list of strings
#This includes the \n at the end of each line
#This is why printing out each line has an extra space 
with open('the-zen-of-python.txt') as f:
    fileLines = f.readlines()
    print(type(fileLines))
    for line in fileLines:
        print (line)
        #To avoid the extra empty space between lines
        #print (line.strip())

#Reads the text file line by line
with open('the-zen-of-python.txt') as f:
    for line in f:
        print(line.strip())

#UTF-8 encoded files can contain Unicode characters
with open('quotes.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())