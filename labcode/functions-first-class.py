
def greet(name):
    print("Hello, " + name)

#Call the function in the usual way
greet("Spiderman")

#Assign the function (an object) to a variable
say_hello = greet

#Use the variable to call the function in the same way
say_hello("Superman")


#This function accepts another function as its parameter
#And uses this function in its body
def check_val(x, myFunc):
    result = myFunc(x)
    if result > 10:
        print ("That's a large number")
    else:
        print ("That's a small number")
    
def double(n): 
    return 2*n

def triple(n): 
    return 3*n

#Calling check_val and passing it the double function
check_val(4,double)

#Calling check_val and passing it the triple function
check_val(4,triple)


#This function contains two nested functions defined within its body
#It chooses to return one of these functions depending on a condition

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

#Get back one of the functions from get_speak_func and use it
custom_func = get_speak_func(0.2)
print(custom_func("The Most Amazing Python"))

custom_func = get_speak_func(0.8)
print(custom_func("The Most Amazing Python"))

