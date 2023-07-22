
# Q1

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


# Q2

def long_words(n, word_list):
    newlist = []
    for x in word_list:
        if len(x) > n:
            newlist.append(x)
    return newlist	

print(long_words(3, "The quick brown fox jumps over the lazy dog".split()))

# Alternative solution using list comprehension

def long_words(n, word_list):
    newlist = [x for x in word_list if len(x) > n]
    return newlist	

print(long_words(3, "The quick brown fox jumps over the lazy dog".split()))

# Q3

num_list = [12, 20, 37, 48, 60, 59, 17]

def remove_even(num_list):
    newList = []
    for x in num_list:
        if x % 2 == 1:
            newList.append(x)
    return newList   

newList = remove_even(num_list)
print (newList)       

# Alternative solution using list comprehension

num_list = [12, 20, 37, 48, 60, 59, 17]

def remove_even(num_list):
    newList = [x for x in num_list if x % 2 == 1]
    return newList

newList = remove_even(num_list)
print (newList)

# Note that this does not work due to the way that the in loop 
# works in conjunction with the remove method 

num_list = [12, 20, 37, 48, 60, 59, 17]

def remove_even(num_list):
    for num in num_list:
        if num % 2 == 0:
            num_list.remove(num)
    return num_list


newList = remove_even(num_list)
print (newList)

# Q4

def common_member(a, b):
    newList = []
    for i in a:
        if i in b:
            newList.append(i)
    return newList
 
a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9]
 
print("The common elements in the two lists are: ")
print(common_member(a, b))

# solution using list comprehension

def common_member(a, b):
    result = [i for i in a if i in b]
    return result
 
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9]
 
print("The common elements in the two lists are: ")
print(common_member(a, b))

# solution using set


def common_member(a, b):   
    a_set = set(a)
    b_set = set(b)
    return a_set.intersection(b_set)
 
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9]
 
print("The common elements in the two lists are: ")
print(common_member(a, b))


#Q5

def different_member(a, b):
    newList = []
    for i in a:
        if i not in b:
            newList.append(i)
    for i in b:
        if i not in a:
            newList.append(i)
    return newList        
 
a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 1, 2]
 
print("The different elements from the two lists are : ")
print(different_member(a, b))


# Using list comprehension

def different_member(a, b):
    firstList = [i for i in a if i not in b]
    secondList = [i for i in b if i not in a]
    return firstList + secondList
 
a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 1, 2]
 
print("The different elements from the two lists are : ")
print(different_member(a, b))

# Using union of set differences

def different_member(a, b):
    seta = set(a)
    setb = set(b)
    diffa = seta.difference(setb)
    diffb = setb.difference(seta)
    return diffa.union(diffb)

 
a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 1, 2]
 
print("The different elements from the two lists are : ")
print(different_member(a, b))

#Q6


def check_same(someList):
    
    itemToCheck = someList[0]
    for i in someList:
        if i != itemToCheck:
            return False
    return True

 
print(check_same(['a', 'b', 'c']))
print(check_same([8, 8, 8]))


# alternative solution using list comprehension and all function


def check_same(someList):
    return all(i == someList[0] for i in someList)
    
print(check_same(['a', 'b', 'c']))
print(check_same([8,8,8]))


# alternative solution using set

def check_same(someList):
    return len(set(someList)) == 1
    
print(check_same(['a', 'b', 'c']))
print(check_same([8,8,8]))

# alternative solution using count

def check_same(someList):
   return someList.count(someList[0]) == len(someList)
    
print(check_same(['a', 'b', 'c']))
print(check_same([8,8,8]))


#Q7

def find_item_count(someList):
   frequency = {}
   for item in someList:
       if item in frequency:
          frequency[item] += 1
       else:
          frequency[item] = 1
   return frequency
   

someList = [10, 20, 10, 30, 20, 20, 20, 20, 40, 40, 50, 50, 10]    
print(find_item_count(someList))
    
# Alternative solution using Collections module

import collections

def find_item_count(someList):
   frequency = collections.Counter(someList)
   return frequency
   

someList = [10, 20, 10, 30, 20, 20, 20, 20, 40, 40, 50, 50, 10]    
print(find_item_count(someList))

#Q8 

def sort_tuples(someList, n):
   someList.sort(key=lambda a: a[n])
   return someList
   

someList = [ (2, 5), (1, 2), (4, 4), (5, 3), (3, 1) ] 
select = int(input("Which element of tuple to sort on: (1)st or (2)nd : "))
print(sort_tuples(someList, select-1))

