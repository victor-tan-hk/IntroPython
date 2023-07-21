
myname = "superman"

myage = 35

def get_net_price(price, tax_rate, discount=0):
    return price * (1 + tax_rate) * (1-discount)


def get_tax(price, tax_rate=0.5):
    print ("get_tax from pricing module called")
    return price * tax_rate