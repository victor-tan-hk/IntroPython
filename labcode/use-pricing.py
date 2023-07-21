

#Method 1: Import the module by its name and then
#reference the required functions or variables through
#the dot operator
import pricing

print (pricing.myage)

net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

#Method 2: Import the module and associate an alias 
#with it and then reference the functions / variables
#in the same way

import pricing as selling_price

net_price = selling_price.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

#Method 3: Use from in order to explicitly specify the 
#functions you want to use, so the dot operator is 
#no longer necessary

from pricing import get_net_price

net_price = get_net_price(price=100, tax_rate=0.01)
print(net_price)

#Method 4: Use from as in Method 3 but rename the imported
#function

from pricing import get_net_price as calculate_net_price

net_price = calculate_net_price(
    price=100,
    tax_rate=0.1,
    discount=0.05
)
print(net_price)

#Method 5: Import everything from module with *
#This can be problematic if there are name conflicts
#between multiple imported modules
#the most recently imported module will take precedence
#Compiler will typically give warning

from pricing import *
from product import *


#can access variables directly
print (myname)
print (myage)

result = get_tax(100)
print(result)

#Tells us where the current module search path is at:
import sys

for path in sys.path:
    print (path)


