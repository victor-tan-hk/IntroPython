

#The Global Namespace consists of the all variables defined at the main level of the program.

#global variable
counter = 10


#A Local Namespace gets created when a local function is invoked. 
#Objects declared in this namespace cannot be used outside the function

def someFunc():
    a = 20
    print (a)
    #Global variables can be accessed anywhere
    print (counter)

print ("Calling someFunc")    
someFunc()

#Uncomment the statement below to see the error
#print (a)



#Namespaces form the following scope hierarchy: Local > Global > Built-In
#If there are 2 or more variables with the same name, 
#the variable higher in the scope hierarchy will be used.

def coolFunc():
    counter = 30
    print(counter)
    
print ("\nCalling coolFunc")    
coolFunc()
print ("The global value of counter is", counter)


#To access global variables within a function, use keyword global

def hotFunc():
    #This references the global variable counter
    global counter
    counter = 50
    print (counter)

print ("\nCalling hotFunc")    
hotFunc()
print ("The global value of counter is", counter)



a = 0
def outerFunc():
    a = 1 # defined under outerfunc
    def innerFunc():
        a = 2
        print("a inside innerFunc is", a)
    
    innerFunc()
    print("a inside outerFunc is", a)
    
print ("\nCalling outerFunc")    
outerFunc()
#This will always reference the global a
print("The global value of a is ", a)


# To access local variables within a nested function body
# use keyword nonlocal
b = 0
def largerFunc():
    b = 1 # defined under outerfunc
    def smallerFunc():
        nonlocal b
        b = 2
        print("b inside smallerFunc is", b)

    
    smallerFunc()
    print("b inside largerFunc is", b)
    
print ("\nCalling largerFunc")    
largerFunc()
#This will always reference the global b
print(b)
print("The global value of b is ", b)

