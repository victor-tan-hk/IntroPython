#A variable is a pointer / reference to an object
#We can use the id function to 
#get the memory address of the object
#that a variable is referring to

print ("\n\n*** Demo working with immutable objects ****")
a = "cat"
b = "cat"
print ("Memory address of object that a references is : ", id(a))
print ("Memory address of object that b references is : ", id(b))

#Notice that both a and b are referring to the same object
c = "dog"
print ("Memory address of object that c references is : ", id(c))

b = c
print ("After assigning c to b (which makes b point to the same object as c)")
print ("Memory address of object that b references is : ", id(b))
print ("Memory address of object that a references is : ", id(a))
print (f"a is {a}, b is {b}, c is {c}")

#Any kind of operation on an immutable object 
#produces a new immutable object
#The original object does not change
d = c.upper() 
print ("After executing an operation on c")
print ("Memory address of object that c references is : ", id(c))
print ("Memory address of object that d references is : ", id(d))
print (f"a is {a}, b is {b}, c is {c}, d is {d}")


print ("\n\n*** Demo working with mutable objects ****")
d = [1, 2, 3]
e = d
print ("After assigning d to e (which makes e point to the same object as d)")
print ("Memory address of object that d references is : ", id(d))
print ("Memory address of object that e references is : ", id(e))
print (f"d is {d}, e is {e}")

#Any kind of operation on a mutable object 
#changes that object without creating a new object
d[0] = 100
d.append(4)
print ("After executing an operation on d")
print ("Memory address of object that d references is : ", id(d))
print ("Memory address of object that e references is : ", id(e))
print (f"d is {d}, e is {e}")

#This creates a new list object and makes d point to it
#e is still point to the previous list object
d = [21, 22, 23]
print ("After making d point to a new object")
print ("Memory address of object that d references is : ", id(d))
print ("Memory address of object that e references is : ", id(e))
print (f"d is {d}, e is {e}")



def changeNum(x):
    print ("Memory address of object that x references is : ", id(x))
    #Since numbers are immutable objects
    #Any operation on them produces a new immutable object
    x = x + 15
    print ("x inside changeNum is now ", x)
    print ("Memory address of object that x references is : ", id(x))
    
print ("\n\n*** Demo calling function with immutable object ****")
age = 30
print ("Memory address of object that age references is : ", id(age))
print("Before calling changeNum, age is : ", age)
changeNum(age)
print ("Memory address of object that age references is : ", id(age))
print ("After calling changeNum, age is : ", age)  



def changeList(y):
    print ("Memory address of object that y references is : ", id(y))
    #Since lists are mutable objects
    #Any operation on them changes the original object
    
    y[0] = 100
    y.append(4)
    print ("y inside changeList is now ", y)
    print ("Memory address of object that y references is : ", id(y))


print ("\n\n*** Demo calling function with mutable object ****")
nums = [1, 2, 3]
print ("Memory address of object that nums references is : ", id(nums))
print("Before calling changeList, nums is : ", nums)
changeList(nums)
print ("Memory address of object that nums references is : ", id(nums))
print("After calling changeList, nums is : ", nums)



def changeListDifferent(z):
    print ("Memory address of object that z references is : ", id(z))
    #Since lists are mutable objects
    #Any operation on them changes the original object
    z[0] = 100
    z.append(4)
    
    #However if reassign z 
    #the a new object is created
    z = [21, 22, 23]
    
    print ("z inside changeList is now ", z)
    print ("Memory address of object that z references is : ", id(z))


print ("\n\n*** Demo calling function with mutable object and reassignment in function body ****")
nums = [1, 2, 3]
print ("Memory address of object that nums references is : ", id(nums))
print("Before calling changeListDifferent, nums is : ", nums)
changeListDifferent(nums)
print ("Memory address of object that nums references is : ", id(nums))
print("After calling changeListDifferent, nums is : ", nums)
