
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y==0:
        raise ValueError('can not divide by zero')
    return x / y