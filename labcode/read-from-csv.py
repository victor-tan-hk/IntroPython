import csv

#Read the CSV file as is
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)
        

#If the first line is the header
#you can use enumerate to get the index of each line
#and determine which line is the header

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(f"{line_no} : {line}")  # data
            
#Another quick and easy way is to just simply skip
#the first line

#You can also store the contents of the CSV into a list
#creating a nested list

countries = []

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the first row
    next(csv_reader)

    # store the data in appropriate format
    # the 2nd item in each list should be changed
    # to a number
    for line in csv_reader:
        strnum = float(line[1])
        del line[1]
        line.insert(1, strnum)
        countries.append(line)            

#Some sample processing that can be performed on a CSV file
print ("\n\nFinding average area of all countries")
total_area = 0
for country in countries:
    total_area += country[1]
print (total_area / len(countries))  

      
print ("\n\nFind all countries with area > 2000000")
large_countries = list(filter(lambda x : x[1] > 2000000, countries))
print ("Display them in sorted order")
large_countries.sort(key=lambda x: x[1])

for country in large_countries:
    print (country)

print ("\n\nFind the frequency for country codes for each letter of the alphabet")
dict_code = { }
for asciicode in range (65,91):
    dict_code[chr(asciicode)] = 0
print ("Initialized dict_code", dict_code)
for country in countries:
    dict_code[country[2][0]] = dict_code[country[2][0]] + 1
print ("Showing frequency for country codes in sorted order")
sorted_dict_list = sorted(dict_code.items(), key = lambda x : x[1])
for item in sorted_dict_list:
    print (f"{item[0]} : {item[1]}")



#You can also read a CSV file in the form of a dictionary

# import csv

# with open('country.csv', encoding="utf8") as f:
#     csv_reader = csv.DictReader(f)
#     # skip the header
#     next(csv_reader)
#     # show the data
#     for line in csv_reader:
#         print (line)
 


