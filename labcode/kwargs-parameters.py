
##The ** indicates a keyword parameter
#This accept a variable number of keyword arguments 
# as a dictionary.
#It can also accept a dictionary directly

def show_details(**config):
    print (type(config))
    for k, v in config.items():
        print(f"{k}: {v}")

print ("Calling the function using keyword arguments")

show_details(os = "Windows", version = "11", cpu = "Intel")
    
print ("Calling the function using a dictionary")

config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'superman'}

#Note we have to unpack it first into separate keyword arguments before 
#sending
show_details(**config)


# If a function has the **kwargs parameter and other parameters, 
# you need to place the **kwargs after other parameters. 
# Otherwise, you’ll get an error.

#This is perfectly fine
def demo1(x, **kwargs):
    print(kwargs)
    
#This is NOT OK
# def demo2(**kwargs, x):
#     print(kwargs)

    
# You can combine both the *args and **kwargs parameters
# in a single function


def coolFunc(*args, **kwargs):
    print (args)
    print (kwargs)
    
#You must ensure the keyword arguments are after the positional arguments
coolFunc(1, 2, 3, os = "Windows", version = "11", cpu = "Intel")    
       
#This will not work
#coolFunc(os = "Windows", version = "11", cpu = "Intel", 1, 2, 3 )    

    

