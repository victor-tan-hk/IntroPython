

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#Takes all elements from index 1 to 3 (1 less than the end)
sub_colors = colors[1:4]
print("Demo 1: ",sub_colors)

#Take all elements from index 3 until the list end
sub_colors = colors[3:]
print("Demo 2: ",sub_colors)

#Gets the first 3 elements from the list
sub_colors = colors[:3]
#This is shortform for writing colors[0:3]
print("Demo 3: ", sub_colors)

#Gets the last 3 elements from the list
sub_colors = colors[-3:]
print("Demo 4: ", sub_colors)

#Get a sublist that includes every 2nd element of the list
sub_colors = colors[::2]
print("Demo 5: ", sub_colors)

#Get a sublist that between index 1 and 5 that includes 
#every 2nd element 
sub_colors = colors[1:5:2]
print("Demo 6: ", sub_colors)

#Reversing a list
sub_colors = colors[::-1]
print("Demo 7: ", sub_colors)

#Subsitute items in index 2 and 3 with new values from a list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[2:4] = ['black', 'white']
print("Demo 8: ", colors)


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(f"The list has {len(colors)} elements")

#Substitute items in index 0 and 1 with 2 new values and insert
#a new extra value (gray)
colors[0:2] = ['black', 'white', 'gray']
print("Demo 9: ", colors)
print(f"The list now has {len(colors)} elements")

#Using del with slicing to delete elements
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#Delete items from index position 2 to 4
del colors[2:5]
print("Demo 10: ", colors)

