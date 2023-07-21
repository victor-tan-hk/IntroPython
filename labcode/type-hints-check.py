
#addItems expects to get int parameters and 
#return an int result
def addItems(x, y):
    return x + y


#This works as expected
result = addItems(3, 5)
print (f"The first result from addItems is {result}")

#This still works even though we pass incorrect
#parameter types, as we can still use the +
#operator on strings (concatenation)
result = addItems("cat", "dog")
print (f"The second result from addItems is {result}")


#divideItems expects to get int parameters and 
#return an int result
def divideItems(x, y):
    return x / y

#This works as expected
result = divideItems(6, 2)
print (f"The first result from divideItems is {result}")

#This no longer works 
#because the / operator does not work on strings

#result = divideItems("cat", "dog")

#One way to work around this is to perform
#explicit type checking in the body of the function
#and only execute the type sensitive code 
#if the parameters are of correct type
def divideItemsWithCheck(x, y):
    if isinstance(x,int) and isinstance(y,int):
        return x / y
    else:
        print("x and y must be integers! ")
        
#This works as expected
result = divideItemsWithCheck(6, 2)
print (f"The first result from divideItemsWithCheck is {result}")

#The attempt below results in function giving a warning
#Notice that when you try to assign the return result
#from a function that doesn't return a result, you get None
#This is a special data type that is used to mean null or no value
result = divideItemsWithCheck("cat", "dog")
print (f"The second result from divideItemsWithCheck is {result}")

#Demonstrating the use of type hints
def divideItemsWithTypeHint(x : int , y : int ) -> float:
    return x / y

#This works as expected
result = divideItemsWithTypeHint(6, 2)
print (f"The first result from divideItemsWithTypeHint is {result}")


#Comment out code below to be able to see errors
#flagged by the static type checking tool

#result = divideItemsWithTypeHint("cat", "dog")

#This will still be executed and cause an error
#Type hints only allows static type checking
#It DOES NOT override Python's dynamic typing behavior


#Another form of type hint
#This is known as variable annotations

name: str = 'Hello'
#No need for type hint, static tool can infer
#that age is of type int based on assigned value
age = 35

#The typing module allows you to perform 
#variable annotation with more complex data types
from typing import List, Dict

names: List[str] = ['Bob', 'Mark', 'Jack']
    
emails: Dict[str, str] = {
    'Bob': 'bob@email.com',
    'Mark': 'mark@email.com',
    'Jack': 'jack@email.com'
}


#Comment out code below to be able to see errors
#flagged by the static type checking tool
#due to assignment of incompatible types

#name = 100
#age = 'superman'
#names.append(20)
#emails['Bob'] = 200

